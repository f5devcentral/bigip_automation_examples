import copy
import json


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
    "name": "unknown",
    "parameterLocation": "any",
    "performStaging": False,
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

def get_policy(policy_master_copy, policy_name):
    for policy in policy_master_copy.get('results', []):
        if policy.get('item') == policy_name and policy.get('status') == 200:
            return policy.get('json')
    return None

class FilterModule(object):
    def filters(self):
        return {
            'zip_to_policy': self.zip_to_policy
        }

    def zip_to_policy(self, data, policy_master_copy):
        policies = {}
        log = {}
        for override in data:
            policyNames = override.get('name', '')
            if isinstance(policyNames, str):
                policyNames = [policyNames]

            for policyName in policyNames:
                policies[policyName] = get_policy(policy_master_copy, policyName)
                log[policyName] = []
                for parameter in override.get('parameters', {}):
                    parameter_info = copy.deepcopy(default_parameter)
                    parameter_info["name"] = parameter["name"]
                    found = False
                    policy_parameters = policies[policyName]["declaration"]["policy"].get('parameters', [])

                    for entry in policy_parameters:
                        if entry["name"] == parameter["name"]:
                            found = True
                            parameter_info = entry
                            log[policyName].append({"name": parameter["name"], "operation": "Update"})
                    if found == False:
                        policy_parameters.append(parameter_info)
                        log[policyName].append({"name": parameter["name"], "operation": "Add"})

                    signature_overrides = parameter_info.get('signatureOverrides', [])
                    for signature in parameter["signatures"]:
                        signature_entry = copy.deepcopy(default_signature_override)
                        signature_entry["signatureId"] = signature
                        add_item_if_not_present(signature_overrides, signature_entry, 'signatureId')

                    policies[policyName]["declaration"]["policy"]["parameters"] = policy_parameters

        return {"policies": policies, "log": log}
