from ansible.module_utils.converter_context import LtmPolicyConverterFactory

class LtmPolicyConverter:
    def __init__(self, ltm_policy):
        self.ltm_policy = ltm_policy.get("ltm_policy", {})
    
    def convert(self):
        rValue = []
        policy_type = self.ltm_policy.get("type", "")
        if policy_type != "ltm_policy":
            raise Exception("Not supported ltm policy type: " + policy_type)

        requires = self.ltm_policy.get("requires", [])
        if len(requires) != 1:
            raise Exception("Not supported policy field value [requires]: " + requires)

        policy_protocol = requires[0]
        policy_converter_factory = LtmPolicyConverterFactory().policyConverter.get(policy_protocol, None)
        if policy_converter_factory is None:
            raise Exception("Not supported policy field value [requires]: " + requires)

        rules = self.ltm_policy.get("rules", [])
        for rule in rules:
            actions = rule.get("actions", [])
            conditions = rule.get("conditions", [])
            name = rule.get("rule_name", "")
            context = ConverterContext(actions, conditions)

            for condition in conditions:
                first_clause = condition["block"][0]

                condition_converter = policy_converter_factory.conditionConverterFactory.get(first_clause, None)
                if condition_converter is None:
                    raise Exception("Not supported condition: ", first_clause)

                condition_converter(context, condition)

            for action in actions:
                first_clause = action["block"][0]

                action_converter = policy_converter_factory.actionConverterFactory.get(first_clause, None)
                if action_converter is None:
                    raise Exception("Not supported action: ", first_clause)

                action_converter(context, action)

            rValue.append(context.irule)

        return rValue
