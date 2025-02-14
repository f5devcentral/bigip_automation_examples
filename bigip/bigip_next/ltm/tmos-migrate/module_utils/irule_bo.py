class ActionClause:
    def __init__(self, action):
        self.action = action

    def toString(self, space=""):
        return space + self.action

class IfClause:
    def __init__(self, condition, body=None, otherwise=None):
        self.condition = condition
        self.ifs = []
        self.body = [] if body is None else body
        self.otherwise = [] if otherwise is None else otherwise

    def toString(self, space=""):
        rValue = space
        rValue = rValue + f"if {{ {self.condition} }} {{\r\n"
        
        for bodyItem in self.body:
            rValue = rValue + bodyItem.toString(space + "  ")
            rValue = rValue + "\r\n"

        for ifClause in self.ifs:
            rValue = rValue + ifClause.toString(space + "  ")
            rValue = rValue + "\r\n"

        rValue = rValue + space + "}\r\n"

        if len(self.otherwise) > 0:
            rValue = rValue + space + "else {\r\n"
            for otherwiseAction in self.otherwise:
                rValue = rValue + otherwiseAction.toString(space + "  ")
                rValue = rValue + "\r\n"
            rValue = rValue + space + "}\r\n"
        return rValue

class WhenClause:
    def __init__(self, when_type):
        self.when_type = when_type
        self.ifs = []

    def toString(self, space=""):
        if len(self.ifs) == 0:
            return ""

        rValue = ""
        rValue = f"when {self.when_type} {{\r\n"
        for ifClause in self.ifs:
            rValue = rValue + ifClause.toString("  ")
        rValue = rValue + "}"
        return rValue


class IRule:
    def __init__(self):
        self.ruleName = ""
        self.request = WhenClause('HTTP_REQUEST')
        self.response = WhenClause('HTTP_RESPONSE')

    def setRuleName(self, name):
        self.ruleName = name

    def getRuleName(self):
        items = self.ruleName.split("/")
        return items[len(items) - 1]

    def getRulePath(self):
        return self.ruleName

    def toString(self, space=""):
        rValue = ""

        rValue = self.request.toString()
        rValue = rValue + "\r\n\r\n"
        rValue = rValue + self.response.toString()

        return rValue

    def toDict(self):
        content = self.toString()
        return {
            "name": self.getRuleName(),
            "content": content,
            "content_utf": content.encode("utf-8"),
            "path": self.getRulePath()
        }
