class FilterModule(object):
    def filters(self):
        return {
            'get_apps_to_import_dependencies': self.get_apps_to_import_dependencies
        }

    def update_server_list_by_object(self, data, server_object_name, installed_objects_list, server_list):
        obj_to_create = []
        for server in data:
            for obj_name in list(map(lambda item: item["old_name"], server[server_object_name])):
                if obj_name not in obj_to_create and obj_name not in installed_objects_list and server['id'] not in server_list:
                    obj_to_create.append(obj_name)
                    server_list.append(server['id'])

    def get_apps_to_import_dependencies(self, data, installed_irules, installed_certificates):
        if len(installed_irules) == 0 or len(installed_certificates) == 0:
            return list(map(lambda server: server['id'], data))

        rValue = []
        self.update_server_list_by_object(data, 'irules', installed_irules, rValue)
        self.update_server_list_by_object(data, 'cert', installed_certificates, rValue)

        return rValue
