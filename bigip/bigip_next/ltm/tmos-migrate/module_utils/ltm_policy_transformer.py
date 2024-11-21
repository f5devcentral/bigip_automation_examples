from lark import Lark, Transformer

# Define the BNF grammar for the LTM policy
ltm_policy_grammar = r"""
    start: ltm_policy

    ltm_policy: "ltm policy" IDENTIFIER "{" descriptor+  "}"
    descriptor: (controls | requires | rules | strategy)+

    controls: "controls" "{" control_values "}"
    requires: "requires" "{" require_values "}"
    rules: "rules" "{" rule "}"
    strategy: "strategy" IDENTIFIER

    control_values: IDENTIFIER+
    require_values: IDENTIFIER+

    rule: IDENTIFIER "{" actions conditions description?"}"

    actions: "actions" "{" action_block+ "}"
    action_block: NUMBER "{" (string | IDENTIFIER)+ "}"

    conditions: "conditions" "{" condition_block+ "}"
    condition_block: NUMBER "{" condition+ "}"
    condition: (complex_condition | string | IDENTIFIER)+
    complex_condition: IDENTIFIER "{" (string | IDENTIFIER)+ "}"

    description: "description" IDENTIFIER+

    string: "\"" STRING "\""
    STRING: /[^"]+/
    IDENTIFIER: /[a-zA-Z0-9\/_.-]+/s
    NUMBER: /\d+/

    %import common.WS
    %ignore WS
"""

class LTMPolicyTransformer(Transformer):
    def start(self, items):
        return {'ltm_policy': items[0]}

    def get_by_name(self, arr, name):
        for item in arr:
            if item["name"] == name:
                return item["data"]

        return None

    def ltm_policy(self, items):
        return {
            "type": "ltm_policy",
            "name": items[0],
            "controls": self.get_by_name(items[1], "controls"),
            "requires": self.get_by_name(items[1], "requires"),
            "rules": self.get_by_name(items[1], "rules"),
            "strategy": self.get_by_name(items[1], "strategy")
        }

    def descriptor(self, items):
        return  items
    
    def controls(self, items):
        return {"name": "controls", "data": items[0]}
    
    def requires(self, items):
        return {"name": "requires", "data": items[0]}
    
    def rules(self, items):
        return {"name": "rules", "data": items}
    
    def rule(self, items):
        return { "rule_name": items[0], "actions": items[1], "conditions": items[2], "description": items[3] if len(items) > 3 else None }
    
    def actions(self, items):
        return items
    
    def action_block(self, items):
        return {"index": items[0], "block": items[1:]}

    def conditions(self, items):
        return items
    
    def condition_block(self, items):
        return {"index": items[0], "block": items[1]}

    def condition(self, items):
        return items

    def complex_condition(self, items):
        return {"name": items[0], "block": items[1:]}
    
    def strategy(self, items):
        return {"name": "strategy", "data": items[0]}
    
    def control_values(self, items):
        return items
    
    def require_values(self, items):
        return items

    def description(self, items):
        return items
    
    def string(self, items):
        return items[0]

    def STRING(self, token):
        return str(token)

    def IDENTIFIER(self, token):
        return str(token)
    
    def NUMBER(self, token):
        return int(token)

# Create the Lark parser
parser = Lark(ltm_policy_grammar, start='start', parser='lalr', transformer=LTMPolicyTransformer())

# Function to parse the LTM policy
def parse_ltm_policy(policy_str):
    return parser.parse(policy_str)

# Function to convert the parsed LTM policy to an iRule
def convert_to_irule(parsed_policy):
    return irule

