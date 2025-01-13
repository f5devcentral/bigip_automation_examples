import json

class FilterModule(object):
    def filters(self):
        return {
            'append_object_if_required': self.append_object_if_required,
            'update_ip_if_required': self.update_ip_if_required,
            'fix_monitor_defaults': self.fix_monitor_defaults
        }

    def append_object_if_required(self, as3_request_data, next_migration_apps, migration_waf_prefix):
        as3_app_definition = json.loads(as3_request_data["content"])

        for migrate_app in next_migration_apps['json']['_embedded']['applications']:
            if as3_request_data['item'] == migrate_app['as3_preview']:
                applications = self.find_node(as3_app_definition, 'Application')
                application_node = applications[0]
                for virtual_server in migrate_app['virtual_servers']:
                    if len(virtual_server.get('waf_policies', [])) > 0:
                        migrate_waf_name = virtual_server['waf_policies'][0]['old_name'].replace('/Common/', migration_waf_prefix)
                        vs_name = virtual_server['name']
                        application_node[vs_name]['policyWAF'] = {
                            'cm': migrate_waf_name
                        }
                    if len(virtual_server.get('certificates', [])) > 0:
                        migrate_cert_name = virtual_server['certificates'][0]['old_name'].replace('/Common/', migration_waf_prefix)
                        node_cert_name = virtual_server['certificates'][0]['old_name'].replace('/Common/', '')
                        application_node[node_cert_name] = {
                           "certificate": {
                              "cm": migrate_cert_name + ".crt"
                            },
                            "class": "Certificate",
                            "privateKey": {
                              "cm": migrate_cert_name + ".pem"
                            }
                        }
                break

        return as3_app_definition
    
    def fix_monitor_defaults(self, as3_app_definition):
        monitors = self.find_node(as3_app_definition, "Monitor")
        for monitor_definition in monitors:
            monitorType = monitor_definition.get("monitorType", None)
            interval = monitor_definition.get("interval", None)
            receive = monitor_definition.get("receive", None)
            send = monitor_definition.get("send", None)
            timeout = monitor_definition.get("send", None)

            if (monitorType == "http" or monitorType == "https") and interval is None and receive is None and send is None and timeout is None:
                monitor_definition["interval"] = 5
                monitor_definition["receive"] = ""
                monitor_definition["send"] = "GET /\\r\\n"
                monitor_definition["timeout"] = 16
        
        return as3_app_definition

    def update_ip_if_required(self, as3_app_definition, ip_map):
        services = self.find_node(as3_app_definition, 'Service_')
        for service in services:
            virtualAddressesArr = service.get("virtualAddresses", None)
            if virtualAddressesArr is not None:
                for virtualAddressIndex in range(len(virtualAddressesArr)):
                    address = virtualAddressesArr[virtualAddressIndex]
                    if address in ip_map:
                        replace = ip_map[address]
                        virtualAddressesArr[virtualAddressIndex] = replace

        return as3_app_definition
    
    def fix_monitor_defaults(self, as3_app_definition):
        monitors = self.find_node(as3_app_definition, "Monitor")
        for monitor_definition in monitors:
            monitorType = monitor_definition.get("monitorType", None)
            interval = monitor_definition.get("interval", None)
            receive = monitor_definition.get("receive", None)
            send = monitor_definition.get("send", None)
            timeout = monitor_definition.get("send", None)

            if monitorType == "http" and interval is None and receive is None and send is None and timeout is None:
                monitor_definition["interval"] = 5
                monitor_definition["receive"] = ""
                monitor_definition["send"] = "GET /\\r\\n"
                monitor_definition["timeout"] = 16

        return as3_app_definition



    def find_node(self, as3_app_definition, className):
        def recursive_search(d, results):
            if isinstance(d, dict):
                classValue = d.get("class")
                if classValue and classValue.startswith(className):
                    results.append(d)
                for key, value in d.items():
                    recursive_search(value, results)
            elif isinstance(d, list):
                for item in d:
                    recursive_search(item, results)

        results = []
        recursive_search(as3_app_definition, results)
        return results
