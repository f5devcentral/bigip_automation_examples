class ActionClause:
    def __init__(self, action):
        self.action = action

class IfClause:
    def __init__(self, condition, body=None, otherwise=None):
        self.condition = condition
        self.ifs = []
        self.body = [] if body is None else body
        self.otherwise = [] if otherwise is None else otherwise


class WhenClause:
    def __init__(self, when_type):
        self.when_type = when_type
        self.ifs = []

class IRule:
    def __init__(self):
        self.request = WhenClause('HTTP_REQUEST')
        self.response = WhwnClause('HTTP_RESPONSE')
