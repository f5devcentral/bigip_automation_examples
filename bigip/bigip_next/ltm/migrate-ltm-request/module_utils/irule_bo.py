class ActionClause:
    def __init__(self, action):
        self.action = action

class IfClause:
    def __init__(self, condition):
        self.condition = condition
        self.ifs = []
        self.action = []

class WhenClause:
    def __init__(self, when_type):
        self.when_type = when_type
        self.ifs = []
        self.actions = []

class IRule:
    def __init__(self):
        self.request = WhenClause('HTTP_REQUEST')
        self.response = WhwnClause('HTTP_RESPONSE')
