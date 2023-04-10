import json
import os
import sys

# get file handler
f = open('as3.json','r')
  
# returns JSON object as a dictionary
data = json.load(f)

# updating IP address
data["declaration"]["API-Prod"]["API"]["VS_API"]["virtualAddresses"] = [sys.argv[1].replace('\"', '')]
data["declaration"]["API-Prod"]["API"]['pool_NGINX_API_AS3']['members'][0]['serverAddresses'] = [sys.argv[2].replace('\"', '')]
if len(sys.argv) > 3:
    data["declaration"]["API-Prod"]["API"]['pool_NGINX_API_AS3']['members'][0]['servicePort'] = int(sys.argv[3])

# Closing files
f.close()

os.remove("as3.json")
# Writing to as3.json
with open("as3.json", "w") as outfile:
    json.dump(data, outfile)
