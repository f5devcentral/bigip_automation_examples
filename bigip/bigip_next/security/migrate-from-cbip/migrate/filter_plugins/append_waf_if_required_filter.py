import json

class FilterModule(object):
    def filters(self):
        return {
            'append_waf_if_required': self.append_waf_if_required
        }

    def append_waf_if_required(self, as3_request_data, next_migration_apps, migration_waf_prefix):
        as3_app_definition = json.loads(as3_request_data["content"])

        # 1.as_request_data.item find in next_migration_app.json._embedded.applications.as3_preview
        # 2. Enumerate all virtual servers in found application
        # 3. By virtual server name add policyWAF.cm value if the first waf object if virtual server if any. Replace the /common/ with the migration prefix

        for migrate_app in next_migration_apps['json']['_embedded']['applications']:
            if as3_request_data['item'] == migrate_app['as3_preview']:
                application_node = self.find_app_node(as3_app_definition)
                for virtual_server in migrate_app['virtual_servers']:
                    if len(virtual_server['waf_policies']) > 0:
                        migrate_waf_name = virtual_server['waf_policies'][0]['old_name'].replace('/Common/', migration_waf_prefix)
                        vs_name = virtual_server['name']
                        application_node[vs_name]['policyWAF'] = {
                            'cm': migrate_waf_name
                        }
                break

        return as3_app_definition

    def find_app_node(self, as3_app_definition):
        def recursive_search(d):
            if isinstance(d, dict):
                if d.get("class") == "Application":
                    return d
                for key, value in d.items():
                    result = recursive_search(value)
                    if result is not None:
                        return result
            return None

        return recursive_search(as3_app_definition)
