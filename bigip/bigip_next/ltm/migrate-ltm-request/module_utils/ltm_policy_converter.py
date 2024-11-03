from ansible.module_utils.converter_context import LtmPolicyConverterFactory
from ansible.module_utils.converter_context import RuleConverterContext

class LtmPolicyConverter:
    def __init__(self, ltm_policy):
        self.ltm_policy = ltm_policy.get("ltm_policy", {})
    
    def convert(self, tenant, app, vs):
        iRules = []
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

        policy_strategy = self.ltm_policy.get("strategy", "")
        if policy_strategy != "/Common/first-match":
            raise Exception(f"Policy strategy {policy_strategy} is not supported")


        rules = self.ltm_policy.get("rules", [])
        for rule in rules:
            actions = rule.get("actions", [])
            conditions = rule.get("conditions", [])
            name = rule.get("rule_name", "")
            context = RuleConverterContext(tenant, app, vs)

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

            iRules.append(context.irule)
        
        rValue = iRules[0]
        index = 1
        while index < len(iRules):
            currentRule + iRules[i]
            rValue.request.ifs = rValue.request.ifs + iRules[i].request.ifs
            rValue.response.ifs = rValue.response.ifs + iRules[i].response.ifs
        
        rValue.setRuleName(self.ltm_policy.get("name", ""))

        return rValue
