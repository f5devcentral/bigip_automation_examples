import os
import dockerlib


key_name = os.getenv("TF_VAR_EC2_KEY_NAME")
key_name= "automation-key"
cwd = os.getcwd()
print("key_name,cwd:",key_name,"\t",cwd)
nodeip_file_path = cwd + "/nodeip"
print("nodeip_file_path",nodeip_file_path)

file_hand = open(nodeip_file_path, 'r')
nodeip = file_hand.read()

print("nodeip, key_name",nodeip,"\t", key_name)
install_status = dockerlib.deploy_app(nodeip, key_name, pem_file=False)
assert "successfully" in install_status
