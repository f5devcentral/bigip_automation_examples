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

class LtmPolicyMigrate:
    def __init__(self, config_files, applications, migrations, logger):
        self.config_files = config_files
        self.applications = applications
        self.migrations = migrations
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
        self.logger(tenant + ' / '+ app + ' / ' + vs )
        ltm_policies = []
        for cfg in config:
            policies = extract_ltm_policies(cfg["content"])
            for p in policies:
                ltm_policies.append(p)

        try:
            for p in ltm_policies:
                self.logger(p)
                ltm_parsed = parse_ltm_policy(p)

                self.logger(ltm_parsed)

                st = json.dumps(ltm_parsed)
                self.logger(st)
                self.logger('*****************')

                irules = LtmPolicyConverter(ltm_parsed).convert()
                self.logger(irules)

        except Exception as X:
            self.logger("in exception")
            self.logger(X)
            
        return[]

    def migrate_routing_policy(self):
        for migration in self.migrations:
            for vs in migration["virtual_servers"]:
                as3_app_info = self.match_as3app_by_vs_name(migration["name"], vs["name"])
                if as3_app_info is None:
                    continue

                config = self.match_config(vs["config_files"])
                migrated_ltm = self.migrate_ltm_routes(config, as3_app_info["tenant_name"], migration["name"], vs["name"])

                for irule in migrated_ltm:
                    adc = as3_app_info["adc"]
                    adc[as3_app_info["tenant"]][migration["name"]][irule["name"]] = {
                            'iRule': { 'base64': base64.b64encode(irule["content"]) },
                            'class': "iRule"
                    }
                    adc[as3_app_info["tenant"]][migration["name"]][vs["name"]].iRules.append({
                        'use': iRule["path"]
                    })

        return {"success": True, "data": "Migration data here"}

def run_module():
    module_args = dict(
        config_files=dict(type='list', required=True),
        applications=dict(type='list', required=True),
        migrations=dict(type='list', required=True)
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

    def custom_logger(msg):
        with open('../logs/ltm_policy_migration.log', 'a') as f:
            f.write("{0}\n".format(msg))

    try:
        cm = LtmPolicyMigrate(config_files, applications, migrations, custom_logger)
        poll_result = cm.migrate_routing_policy()
        if poll_result["success"]:
            result["success"] = True
            result['message'] = 'LTM policy migration completed.'
            result['data'] = poll_result['data']
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
