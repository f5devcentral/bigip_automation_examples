from lark import Lark, Transformer

# Define the BNF grammar for the LTM policy
ltm_policy_grammar = """
    start: ltm_policy

    ltm_policy: "ltm policy" IDENTIFIER "{" controls? requires rules strategy "}"

    controls: "controls" "{" control_values "}"
    requires: "requires" "{" require_values "}"
    rules: "rules" "{" rule "}"
    strategy: "strategy" IDENTIFIER

    control_values: IDENTIFIER+
    require_values: IDENTIFIER+

    rule: IDENTIFIER "{" actions conditions "}"

    actions: "actions" "{" action_block+ "}"
    conditions: "conditions" "{" condition_block+ "}"

    action_block: NUMBER "{" IDENTIFIER+ "}"
    condition_block: NUMBER "{" ("name" IDENTIFIER)? | ("values" "{" IDENTIFIER+ "}")? | IDNTIFIER+ "}"

    strategy: "strategy" IDENTIFIER

    IDENTIFIER: /[a-zA-Z0-9\/_.-]+/
    NUMBER: /\d+/

    %import common.WS
    %ignore WS
"""

# Define a transformer to convert the parsed tree into a JSON-like dictionary
class LTMPolicyTransformer(Transformer):
def start(self, items):
        return {'ltm_policy': items[0]}

    def ltm_policy(self, items):
        result = {
            'identifier': items[0],
            'controls': items[1] if len(items) > 4 else None,
            'requires': items[2] if len(items) > 4 else None,
            'rules': items[-3],
            'strategy': items[-1]
        }
        return result

    def controls(self, items):
        return {'controls': items[0]}

    def control_values(self, items):
        return items

    def requires(self, items):
        return {'requires': items[0]}

    def require_values(self, items):
        return items

    def rules(self, items):
        return {'rules': items}

    def rule(self, items):
        return {
            'rule_name': items[0],
            'actions': items[1],
            'conditions': items[2]
        }

    def actions(self, items):
        return {'actions': items}

    def action_block(self, items):
        return {'number': items[0], 'actions': items[1:]}

    def conditions(self, items):
        return {'conditions': items}

    def condition_block(self, items):
        condition_dict = {'number': items[0]}
        if len(items) > 1:
            if items[1] == "name":
                condition_dict['name'] = items[2]
            elif items[1] == "values":
                condition_dict['values'] = items[3:]
            else:
                condition_dict['conditions'] = items[1:]
        return condition_dict

    def strategy(self, items):
        return {'strategy': items[0]}

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
    irule = "when HTTP_REQUEST {\n"
    
    # Extract the rules from the parsed policy
    rules = parsed_policy['ltm_policy']['rules']
    for rule_name, rule_content in rules.items():
        condition = rule_content['conditions']
        actions = rule_content['actions']
        
        # Handle condition block (http-host matching)
        for condition_item in condition:
            if condition_item.get("http-host"):
                host_value = condition_item["values"][0]
                irule += f"    if {{[string tolower [HTTP::host]] equals \"{host_value}\"}} {{\n"
        
        # Handle action block (forwarding to pool)
        for action_item in actions:
            if action_item.get("forward"):
                pool_name = action_item["pool"]
                irule += f"        pool {pool_name}\n"
        
        # Close the condition
        irule += "    }\n"
    
    irule += "}"
    return irule

# Example usage: Parse and convert the policy to an iRule
ltm_policy_str = """
ltm policy /tenant1c7deb84161b7/Common_vs-migration/policy-routing {
    controls { forwarding }
    requires { http }
    rules {
        route-fqdn {
            actions {
                0 {
                    forward
                    select
                    pool /Common/nginx
                }
            }
            conditions {
                0 {
                    http-host
                    values { app1.fqdn.com }
                }
            }
        }
    }
    strategy /Common/first-match
}
"""

# Step 1: Parse the LTM policy
parsed_policy = parse_ltm_policy(ltm_policy_str)

# Step 2: Convert the parsed policy to an iRule
irule = convert_to_irule(parsed_policy)

# Output the iRule
print(irule)

