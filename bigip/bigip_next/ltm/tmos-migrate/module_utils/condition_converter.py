import ansible.module_utils.irule_bo
from ansible.module_utils.rnd_string import rnd_string
from ansible.module_utils.irule_bo import IRule
from ansible.module_utils.irule_bo import IfClause
from ansible.module_utils.irule_bo import ActionClause

def httpHostContitionConverter(context, condition):
   values_block = condition["block"][1]
   if values_block.get("name") != "values":
      raise Exception("http-host condition converter clause unsupported: " + values_block)

   hosts = values_block.get("block", [])
   if_conditions = []
   for host in hosts:
      if_conditions.append(f"[HTTP::host] eq \"{host}\"")
   
   rnd_str = rnd_string(3)
   var_name = f"host_match_{rnd_str}"
   if_condition = " or ".join(if_conditions)
   
   requestIf = IfClause(if_condition, [ActionClause(f"set {var_name} 1")], [ActionClause(f"set {var_name} 0")])
   responseIf = IfClause(f"${var_name} == 1")

   context.appendRequestIf(requestIf)
   context.appendResponseIf(responseIf)

def httpHeaderContidionConverter(context, condition):
   add_to_response = False
   index = 0
   block = condition["block"]
   name = ""
   values = []

   while index < len(block):
      item = block[index]
      if isinstance(item, str):
         if item == "response":
            add_to_response = True
         if item == "name":
            name = block[index + 1]
            index = index + 1
      else:
         if item.get("name", "") == "values":
            values = item["block"]
      index = index + 1

   if_conditions = []
   for value in values:
      if_conditions.append(f"[HTTP::header \"{name}\"] eq \"{value}\"")
   
   if_condition = " or ".join(if_conditions)
   if_obj = IfClause(if_condition)

   if add_to_response == True:
      context.appendResponseIf(if_obj)
   else:
      context.appendRequestIf(if_obj)

def httpUriContitionConverter(context, condition):
   block = condition["block"]
   location = block[1]

   if location == "path":
      operation = block[2]
      if_conditions = []
      if_condition = ""
      values = block[3]
      if values["name"] == "values":
         values_block = values["block"]
         for value in values_block:
            if_conditions.append(f"[HTTP::uri] {operation} \"{value}\"")
         if_condition = " or ".join(if_conditions)
         context.appendRequestIf(IfClause(if_condition))
      else:
         raise Exception(f"Not supported values item: {values}")
   
   if location == "query-parameter":
      index = 2
      qry_parameter_name = ""
      qry_parameter_values = []
      while index < len(block):
         item = block[index]
         if isinstance(item, str):
            if item == "name":
               qry_parameter_name = block[index + 1]
               index = index + 1
         else:
            if item.get("name", "") == "values":
               qry_parameter_values = item.get("block", [])
         index = index + 1
      if_operand = " ".join(list(map(lambda x: f"\"{x}\"",qry_parameter_values)))
      if_clause = "[URI::query [HTTP::uri] \"" + qry_parameter_name + "\"] in { " + if_operand + "}"
      context.appendRequestIf(IfClause(if_clause))

