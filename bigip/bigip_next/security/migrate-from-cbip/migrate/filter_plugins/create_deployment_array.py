class FilterModule(object):
    def filters(self):
        return {
                "create_deployment_array": self.create_deployment_array
        }

    def create_deployment_array(self, data, tree):
        rValue = []
        for key, value in data.items():
            deploy_info = tree.get(key, [])
            for info in deploy_info:
                rValue.append({
                    "id": value,
                    "target": info["bigip_next"]
                })

        return rValue
