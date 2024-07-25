class FilterModule(object):
    def filters(self):
        return {
            'shared_object_names': self.shared_object_names
        }

    def shared_object_names(self, data, shared_object_prefix):
        rValue = []
        for server in data:
            if len(server['waf_policies']) > 0:
                rValue.append({
                        'id': server['id'],
                        'waf': server.get('waf_policies', []),
                        'cert': server.get('certificates', [])
                })

        for server in rValue:
            for waf_item in server['waf']:
                waf_item['old_name'] = waf_item['old_name'].replace('/Common/', shared_object_prefix)
            for cert_item in server['cert']:
                cert_item['old_name'] = cert_item['old_name'].replace('/Common/', shared_object_prefix)

        return rValue
