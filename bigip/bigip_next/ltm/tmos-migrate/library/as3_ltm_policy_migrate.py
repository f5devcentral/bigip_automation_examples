from ansible.module_utils.basic import AnsibleModule
import sys
import os
import base64
import json

from ansible.module_utils.config_parser import extract_ltm_policies
from ansible.module_utils.tree_helper import get_node_by_class
from ansible.module_utils.ltm_policy_transformer import parse_ltm_policy
from ansible.module_utils.ltm_policy_transformer import convert_to_irule
from ansible.module_utils.ltm_policy_converter import LtmPolicyConverter

import traceback

class LtmPolicyMigrate:
    def __init__(self, config_files, applications, migrations, pools, monitors, logger):
        self.config_files = config_files
        self.applications = applications
        self.migrations = migrations
        self.pools = pools
        self.monitors = monitors
        self.logger = logger

    def match_config(self, config_files):
        rValue = []
        for _, file_name in enumerate(config_files.values()):
            for cf in self.config_files:
                if cf["item"]["value"] == file_name:
                    rValue.append({
                        'file_name': file_name,
                        'content': cf["content"]
                    })
                    break
        return rValue

    def match_as3app_by_vs_name(self, app_name, vs_name):
        for app in self.applications:
            tenant_name = get_node_by_class(app["json"], "Tenant")
            tenant_info = app["json"][tenant_name]
            if app_name in tenant_info:
                return {
                        'adc': app["json"],
                        'tenant_name': tenant_name
                }
        return None

    def migrate_ltm_routes(self, config, tenant, app, vs):
        ltm_policies = []
        rValue = []
        for cfg in config:
            policies = extract_ltm_policies(cfg["content"])
            for p in policies:
                ltm_policies.append(p)

        try:
            for p in ltm_policies:
                self.logger("Converting policy ==>")
                self.logger(p)
                ltm_parsed = parse_ltm_policy(p)
                rule = LtmPolicyConverter(ltm_parsed).convert(tenant, app, vs)
                irule = rule["rule"]
                self.logger(f"iRule ==> { irule.getRulePath() }")
                self.logger(irule.toString())

                rValue.append(rule)

        except Exception as X:
            self.logger("Convertion error: ")
            self.logger(X)
            self.logger(traceback.format_exc())

        return rValue
    
    def append_pool_info(self, pool, adc, tenant_name, app_name):
        new_path = pool["new"]
        old_path = pool["old"]

        new_path_items = new_path.split("/")
        new_name = new_path_items[len(new_path_items) - 1]
        
        app = adc[tenant_name][app_name]

        if app.get(new_path, None) is not None:
            return
        
        poolFound = False
        for pool_info in self.pools:
            if pool_info["name"] == old_path:
                poolFound = True
                app[new_name] = {
                    "members": pool_info["members"],
                    "class": "Pool",
                    "monitors": []        
                }
                app[f"{new_name}-service"] = {
                    "class": "Service_Pool",
                    "pool": new_name
                }
                # add monitors to pool
                for monitor in pool_info["monitors"]:
                    app[new_name]["monitors"].append({
                        "use": f"/{tenant_name}/{app_name}/{monitor}"
                    })

                    # migrate pool monitors if not migrated
                    monitorFound = False
                    if app.get(monitor, None) is None:
                        for monitor_info in self.monitors:
                            monitorName = monitor_info["name"]
                            self.logger(f"{monitor} --> {monitorName}")
                            if monitor == monitorName:
                                app[monitor] = monitor_info["data"]
                                monitorFound = True                                
                        if monitorFound == False:
                            raise Exception(f"Monitor info {monitor} is required for migration. Please, update variables")
            break # pool info found
        if not poolFound:
            raise Exception(f"Pool info {old_path} is required for migration. Please, update variabled to procees")

    def migrate_routing_policy(self):
        try:
            for migration in self.migrations:
                for vs in migration["virtual_servers"]:
                    as3_app_info = self.match_as3app_by_vs_name(migration["name"], vs["name"])
                    if as3_app_info is None:
                        continue
    
                    config = self.match_config(vs["config_files"])
                    migrated_ltm = self.migrate_ltm_routes(config, as3_app_info["tenant_name"], migration["name"], vs["name"])

                    for migrated_result in migrated_ltm:
                        migrated = migrated_result["rule"]
                        irule = migrated.toDict()
                        adc = as3_app_info["adc"]
                        adc[as3_app_info["tenant_name"]][migration["name"]][irule["name"]] = {
                                'iRule': { 'base64': base64.b64encode(irule["content_utf"]) },
                                'class': "iRule"
                        }
                        virtualServer = adc[as3_app_info["tenant_name"]][migration["name"]][vs["name"]]
                        if virtualServer.get("iRules", None) is None:
                            virtualServer["iRules"] = []

                        tn = as3_app_info["tenant_name"]
                        mn = migration["name"]
                        irn = irule["name"]
                        virtualServer["iRules"].append({
                            'use': f"/{tn}/{mn}/{irn}"
                        })
                    
                        pools = migrated_result["pools"]

                        for pool in pools:
                            self.append_pool_info(pool, adc, tn, mn)
    
            return {"success": True, "results": self.applications}
        except Exception as X:
            self.logger("Convertion error: ")
            self.logger(X)
            self.logger(traceback.format_exc())

            return {"success": False, "results": []}

def run_module():
    module_args = dict(
        config_files=dict(type='list', required=True),
        applications=dict(type='list', required=True),
        migrations=dict(type='list', required=True),
        pools=dict(type='list', required=True),
        monitors=dict(type='list', required=True)
    )

    result = dict(
        changed=False,
        message=''
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    config_files = module.params['config_files']
    applications = module.params['applications']
    migrations = module.params['migrations']
    pools = module.params['pools']
    monitors=module.params['monitors']

    def custom_logger(msg):
        with open('../logs/ltm_policy_migration.log', 'a') as f:
            f.write("{0}\n".format(msg))

    try:
        cm = LtmPolicyMigrate(config_files, applications, migrations, pools, monitors, custom_logger)
        poll_result = cm.migrate_routing_policy()
        if poll_result["success"]:
            result["success"] = True
            result['message'] = 'LTM policy migration completed.'
            result['results'] = poll_result['results']
        else:
            result['message'] = 'LTM policy migration error.'
            result['success'] = False
            module.fail_json(msg='LTM policy migration error.', **result)
    except Exception as e:
        module.fail_json(msg='Error: {0}'.format(str(e)), **result)

    module.exit_json(**result)

def main():
    run_module()

if __name__ == '__main__':
    main()
