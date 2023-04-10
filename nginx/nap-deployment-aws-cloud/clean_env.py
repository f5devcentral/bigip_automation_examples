'''clean infra env key before running scripts.'''

import os
import json
import awslib
from var import *


cwd = os.getcwd()
print(" CWD: " , cwd)
data_dir = cwd+"/data/"
print(" DATADir: " , data_dir)
testbed_data_path = data_dir + "testbed-data.json"
testbed_data = json.load(open(testbed_data_path, 'r'))
ec2_key_name = TF_VAR_EC2_KEY_NAME 
print("ec2_key_name:",ec2_key_name)

#awslib.del_kpair(ec2_key_name)
