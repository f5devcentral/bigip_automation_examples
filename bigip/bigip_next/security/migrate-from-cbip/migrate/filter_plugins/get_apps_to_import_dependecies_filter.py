class FilterModule(object):
    def filters(self):
        return {
            'get_apps_to_import_dependencies': self.get_apps_to_import_dependencies
        }
    
    def get_apps_to_import_dependencies(self, data, installed_waf_names):
        if len(installed_waf_names) == 0:
            return list(map(lambda server: server['id'], data))

        rValue = []
        waf_to_create = []
        for server in data:
            for waf_name in list(map(lambda item: item["old_name"], server['waf'])):
                if waf_name not in installed_waf_names and waf_name not in waf_to_create:
                    rValue.append(server['id'])
                    waf_to_create.append(waf_name)
                    break

        return rValue
