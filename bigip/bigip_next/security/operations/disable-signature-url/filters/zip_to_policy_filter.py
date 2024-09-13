import copy


default_parameter = {
    "allowEmptyValue": False,
    "allowRepeatedParameterName": False,
    "attackSignaturesCheck": True,
    "checkMaxValueLength": False,
    "checkMetachars": True,
    "checkMinValueLength": False,
    "dataType": "alpha-numeric",
    "disallowFileUploadOfExecutables": False,
    "enableRegularExpression": False,
    "isBase64": False,
    "isCookie": False,
    "isHeader": False,
    "level": "global",
    "maximumLength": 10,
    "metacharsOnParameterValueCheck": True,
    "minimumLength": 0,
    "name": "code",
    "parameterLocation": "any",
    "performStaging": False,
    "url": [],
    "sensitiveParameter": False,
    "signatureOverrides": [],
    "type": "explicit",
    "valueType": "auto-detect"
}

default_signature_override = {
    "enabled": False,
    "signatureId": 0,
    "status": "disabled"
}

def add_item_if_not_present(items, new_item, field):
    if not any(item.get(field) == new_item.get(field) for item in items):
        items.append(new_item)
    return items

class FilterModule(object):
    def filters(self):
        return {
            'zip_to_policy': self.zip_to_policy
        }

    def zip_to_policy(self, data):
        rValue = {}
        for override in data:
            policyName = override.get('name', '')
            rValue[policyName] = []
            for parameter in override.get('parameters', {}):
                parameter_info = copy.deepcopy(default_parameter)
                found = False

                for entry in rValue[policyName]:
                    if entry["name"] == parameter["name"]:
                        found = True
                        parameter_info = entry
                if found == False:
                    rValue[policyName].append(parameter_info)

                urls = parameter_info.get('url', [])
                add_item_if_not_present(urls, override["url"], 'name')
                signature_overrides = parameter_info.get('signatureOverrides', [])
                for signature in parameter["signatures"]:
                    signature_entry = copy.deepcopy(default_signature_override)
                    signature_entry["signatureId"] = signature
                    add_item_if_not_present(signature_overrides, signature_entry, 'signatureId')

        return rValue
