import json
import os
import sys

file_list = ['as3.json', 'as3_with_graphql_profile.json', 'as3_with_graphql_pr_introspection.json',
             'as3_str_depth.json']
# get file handler
for c_file in file_list:
    f = open(c_file, 'r')
    # returns JSON object as a dictionary
    data = json.load(f)
    # updating IP address
    data["declaration"]["DVGA_Prod"]["DVGA"]["VS_DVGA"]["virtualAddresses"] = [sys.argv[1].replace('\"', '')]
    data["declaration"]["DVGA_Prod"]["DVGA"]['pool_k8s_nodes']['members'][0]['serverAddresses'] = [
        sys.argv[2].replace('\"', '')]
    if len(sys.argv) > 3:
        data["declaration"]["DVGA_Prod"]["DVGA"]['pool_k8s_nodes']['members'][0]['servicePort'] = int(sys.argv[3])
    # Closing files
    f.close()
    os.remove(c_file)
    # Writing to as3.json
    with open(c_file, "w") as outfile:
        json.dump(data, outfile)
