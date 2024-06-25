class FilterModule(object):
    def filters(self):
        return {
            'waf_app_names': self.waf_app_names
        }

    def waf_app_names(self, data, waf_prefix):
        rValue = []
        for server in data:
            if len(server['waf_policies']) > 0:
                rValue.append({
                        'id': server['id'],
                        'waf': server['waf_policies']
                })

        for server in rValue:
            for waf_item in server['waf']:
                waf_item['old_name'] = waf_item['old_name'].replace('/Common/', waf_prefix)

        return rValue
