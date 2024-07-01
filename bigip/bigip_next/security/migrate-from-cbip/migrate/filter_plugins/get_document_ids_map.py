def extract_service_http_node_name(data):
    def find_service_http_node(node, parent_key=None):
        if isinstance(node, dict):
            if node.get('class', '').startswith('Service'):
                return parent_key
            for key, value in node.items():
                result = find_service_http_node(value, key)
                if result:
                    return result
        elif isinstance(node, list):
            for item in node:
                result = find_service_http_node(item, parent_key)
                if result:
                    return result
        return None

    return find_service_http_node(data)

def remove_prefix(data, prefix):
    new_data = {key.replace(prefix, ''): value for key, value in data.items()}
    return new_data

class FilterModule(object):
    def filters(self):
        return {
            'get_document_ids_map': self.get_document_ids_map
        }

    def get_document_ids_map(self, data, migrate_app_prefix):
        parsed = data["results"]
        rValue = {}
        for request in parsed:
            migrate_vs_name = extract_service_http_node_name(request["item"]["json"])
            if migrate_vs_name is None:
                print(migrate_vs_name)
            document_id = request["json"]["id"]
            rValue[migrate_vs_name] = document_id

        return remove_prefix(rValue, migrate_app_prefix)
