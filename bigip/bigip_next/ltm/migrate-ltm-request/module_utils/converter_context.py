import ansible.module_utils.action_converter
import ansible.module_utils.condition_converter


class RuleConverterContext:
    def __init__(self):
        self.irule = IRule()

class LtmPolicyConverterFactory:
    def __init__(self):
        self.policyConverter = {
            "http": HttpPolicyConverterFactory()
        }

class HttpPolicyConverterFactory:
    def __init__(self):
        self.actionConverterFactory = {
            "http-header": httpHeaderActionConverter,
            "http-set-cookie": httpSetCookieActionConverter,
            "forward": forwardActionConverter,
        }
        self.conditionConverterFactory = {
            "http-host": httpHostContitionConverter,
            "http-header": httpHeaderContidionConverter,
            "http-uri": httpUriContitionConverter
        }
