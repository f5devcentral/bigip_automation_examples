class FilterModule(object):
    def filters(self):
        return {
                "create_deployment_array": self.create_deployment_array
        }

    def create_deployment_array(self, data, tree):
        rValue = []
        for key, value in data.items():
            ip_arr = tree.get(key, [])
            for ip in ip_arr:
                rValue.append({
                    "id": value,
                    "target": ip
                })

        return rValue
