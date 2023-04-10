import os
import dockerlib
import awslib

key_name = os.getenv("TF_VAR_EC2_KEY_NAME")
key_name= "automation-key"
print(key_name)
cwd = os.getcwd()
nap_file_paths = [cwd + "/nap1", cwd + "/nap2"]
ins_ids = [cwd + "/ins1", cwd + "/ins2"]

# deploy app across both instances
for nap_file_path in nap_file_paths:
    file_hand = open(nap_file_path, 'r')
    nodeip = file_hand.read()
    print("=================================== NAP IP is: {0} ===============================".format(nodeip))
    install_status = dockerlib.deploy_app(nodeip, key_name, pem_file=False)
    assert "successfully" in install_status


# restart nginx service with updated nginx conf file
for ins in ins_ids:
    file_hand = open(ins, 'r')
    ins_id = file_hand.read()
    print("=================================== Instance ID is: {0} ===============================".format(ins_id))
    ngx_status = awslib.start_nginx(key_name, "apisecurity-automation-nap", ins_id, pem_file=False)
    print(ngx_status)
