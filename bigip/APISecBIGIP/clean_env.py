'''clean infra env key before running scripts.'''

import os
import json
import awslib


cwd = os.getcwd()
data_dir = cwd+"/data/"
testbed_data_path = data_dir + "testbed-data.json"
testbed_data = json.load(open(testbed_data_path, 'r'))
testbed_data['ec2_key_name'] = os.getenv("TF_VAR_EC2_KEY_NAME")
print("ec2_key_pair=",testbed_data['ec2_key_name'])

awslib.del_kpair(testbed_data['ec2_key_name'])
