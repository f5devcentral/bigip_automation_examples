from ansible.module_utils.irule_bo import ActionClause

def httpHeaderActionConverter(context, action):
    isResponse = False
    headerName = ""
    headerValue = ""

    block = action["block"]

    operation = block[1]
    if operation == "response":
        isResponse = True
        operation = block[2] 

    index = 1
    while index < len(block):
        if block[index] == "name":
            headerName = block[index + 1]
            index = index + 1
        if block[index] == "value":
            headerValue = block[index + 1]
            index = index + 1
        index = index + 1

    action = f"HTTP::header {operation} \"{headerName}\" \"{headerValue}\""
    if isResponse:
        context.appendResponseAction(ActionClause(action))
    else:
        context.appendRequestAction(ActionClause(action))

def httpSetCookieActionConverter(context, action):
    isResponse = False
    headerName = ""
    headerValue = ""

    block = action["block"]

    operation = block[1]
    if operation == "response":
        isResponse = True
        operation = block[2] 

    index = 1
    while index < len(block):
        if block[index] == "name":
            headerName = block[index + 1]
            index = index + 1
        if block[index] == "value":
            headerValue = block[index + 1]
            index = index + 1
        index = index + 1

    action = f"HTTP::cookie {operation} name \"{headerName}\" value \"{headerValue}\""
    if isResponse:
        context.appendResponseAction(ActionClause(action))
    else:
        context.appendRequestAction(ActionClause(action))

def forwardActionConverter(context, action):
    block = action["block"]
    if len(block) > 4:
        raise Exception(f"Unsupported forward block: {block}")
    operation = block[2]

    if block[1] == "select":
        path = block[3]
        poolItems = path.split("/")
        poolName = poolItems[len(poolItems) - 1]
        new_pool_name = f"/app/{context.getTenant()}:{context.getApp()}/pool/{poolName}"
        context.setMigratingPool({
            "old": path,
            "new": new_pool_name
        })
        body = f"{operation} {new_pool_name}-service"
        context.appendRequestAction(ActionClause(body))
