import ansible.module_utils.action_converter
import ansible.module_utils.condition_converter

def addIfClause(ifClause, currentIfClause):
    if len(currentIfClause.ifs) == 0:
        currentIfClause.ifs.append(ifClause)
    else:
        addIfClause(ifClause, currentIfClause.ifs[0])


class RuleConverterContext:
    def __init__(self):
        self.irule = IRule()

    def appendRequestIf(ifClause):
        if len(self.irule.request.ifs) == 0:
            self.irule.request.ifs.append(ifClause)
        else:
            addIfClause(self.irule.request.ifs[0])

    def appendResponseIf(ifClause):
        if len(self.irule.response.ifs) == 0:
            self.irule.response.ifs.append(ifClause)
        else:
            addIfClause(self.irule.response.ifs[0])

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
            "forward": forwardActionConverter
        }
        self.conditionConverterFactory = {
            "http-host": httpHostContitionConverter,
            "http-header": httpHeaderContidionConverter,
            "http-uri": httpUriContitionConverter
        }
