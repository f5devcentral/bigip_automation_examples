import subprocess
import paramiko
from scp import SCPClient
import requests,urllib,re
from bs4 import BeautifulSoup
import json
from var import azure_user_json


#Methods
def az_login(principal,password,tenantid):
    try:  
        chk= subprocess.run("az version", shell = True, stdout=subprocess.PIPE, stderr = subprocess.PIPE)
        sp_create = "az login --service-principal -u " + principal + " -p " + password + " --tenant " + tenantid
        az_cli_login = subprocess.run(sp_create, shell = True, stdout=subprocess.PIPE, stderr = subprocess.PIPE)
        return az_cli_login
    except:
        print(e)
        return False


def change_vm_param_file(param_file, azure_user_json):
    """Change vm deploy params dynamically as per user configuration."""
    param_file_handler = open(param_file, 'r')
    param_file_data = json.load(param_file_handler)
    param_file_handler.close()

    # fetch user details from json
    azure_user_handler = open(azure_user_json,"r")
    azure_user_data = json.load(azure_user_handler)
    azure_user_handler.close()

    # update params in vm deploy template
    param_file_data["parameters"]["location"]["value"] = azure_user_data["location"]
    param_file_data["parameters"]["virtualNetworkId"]["value"] = "/subscriptions/"+azure_user_data["SUBSCRIPTION_ID_ENG"]+"/resourceGroups/"+azure_user_data["CLOUD_CONSOLE_RG"]+"/providers/Microsoft.Network/virtualNetworks/"+azure_user_data["CLOUD_CONSOLE_RG"]+"-vnet"
    param_file_data["parameters"]["virtualMachineRG"]["value"] = azure_user_data["CLOUD_CONSOLE_RG"]
    param_file_data["parameters"]["availabilitySetName"]["value"] = azure_user_data["availabilitySetName"]

    jsonFile = open(param_file, "w+")
    jsonFile.write(json.dumps(param_file_data))
    jsonFile.close()


def change_as_param_file(param_file, azure_user_json):
    """Change avilabilty set deploy params dynamically as per user configuration."""
    param_file_handler = open(param_file, 'r')
    param_file_data = json.load(param_file_handler)
    param_file_handler.close()

    # fetch user details from json
    azure_user_handler = open(azure_user_json,"r")
    azure_user_data = json.load(azure_user_handler)
    azure_user_handler.close()

    # update location param in as deploy json template
    param_file_data["parameters"]["location"]["value"] = azure_user_data["location"]

    jsonFile = open(param_file, "w+")
    jsonFile.write(json.dumps(param_file_data))
    jsonFile.close()


def change_lb_param_files(template_file, param_file, azure_user_json):
    """Change load balancer deploy params dynamically as per user configuration."""
    param_file_handler = open(param_file, 'r')
    param_file_data = json.load(param_file_handler)
    param_file_handler.close()

    # fetch user details from json
    azure_user_handler = open(azure_user_json,"r")
    azure_user_data = json.load(azure_user_handler)
    azure_user_handler.close()

    # update location param in lb param json
    param_file_data["parameters"]["location"]["value"] = azure_user_data["location"]
    jsonFile = open(param_file, "w+")
    jsonFile.write(json.dumps(param_file_data))
    jsonFile.close()

    f = open(template_file, 'r')
    filedata = f.read()
    f.close()

    # update dynamic params in lb deploy json template
    newdata1 = filedata.replace("user-shshaik", azure_user_data["CLOUD_CONSOLE_RG"])
    newdata2 = newdata1.replace("e1e590f6-555e-4dc0-8472-be7fab700b51", azure_user_data["SUBSCRIPTION_ID_ENG"])

    f = open(template_file, 'w')
    f.write(newdata2)
    f.close()


def az_arm_deploy(resource_group, template_file, param_file, azure_user_json=azure_user_json, resource="VM"):
    """Deploy resources in Azure using templates."""
    try:
        if resource == "VM":
            # update vm params as per user config
            change_vm_param_file(param_file, azure_user_json)
        elif resource == "AS":
            # update as params as per user config
            change_as_param_file(param_file, azure_user_json)
        elif resource == "LB":
            change_lb_param_files(template_file, param_file, azure_user_json)

        az_deploy= "az deployment group create --resource-group " + resource_group + " --template-file " + template_file + " --parameters " + param_file + " --output table "   
        print(az_deploy)
        deploy = subprocess.run(az_deploy, shell = True, stdout=subprocess.PIPE, stderr = subprocess.PIPE)
        print(deploy)
        az_dp_out =  deploy.stdout.decode("utf-8")
        az_dp_err =  deploy.stderr.decode("utf-8")
        print(az_dp_out)
        return az_dp_out
    except:
        return az_dp_err
    

def az_get_vm_info(vm_name):
    try:
        az_vm= "az vm list-ip-addresses --output table -n " + vm_name  
        deploy = subprocess.run(az_vm, shell = True, stdout=subprocess.PIPE, stderr = subprocess.PIPE)
        az_vm_out =  deploy.stdout.decode("utf-8")
        az_vm_err =  deploy.stderr.decode("utf-8")
        return az_vm_out
    except:
        return az_vm_err


def az_get_cmd_op(cmd):
    try:
        deploy = subprocess.run(cmd, shell = True, stdout=subprocess.PIPE, stderr = subprocess.PIPE)
        print(deploy)
        az_vm_out =  deploy.stdout.decode("utf-8")
        az_vm_err =  deploy.stderr.decode("utf-8")
        return az_vm_out
    except:
        return az_vm_err


def az_arm_destroy(resource_group,vm_name):
    try:
        az_destroy= "az vm delete --resource-group " + resource_group + " --name " + vm_name + " -y "
        print(az_destroy)
        destroy = subprocess.run(az_destroy, shell = True, stdout=subprocess.PIPE, stderr = subprocess.PIPE)
        az_ds_out =  destroy.stdout.decode("utf-8")
        az_ds_err =  destroy.stderr.decode("utf-8")
        return az_ds_out
    except:
        return az_ds_err


def az_lb_destroy(resource_group,lb_name):
    try:
        az_destroy= "az network lb delete --resource-group " + resource_group + " --name " + lb_name
        print(az_destroy)
        destroy = subprocess.run(az_destroy, shell = True, stdout=subprocess.PIPE, stderr = subprocess.PIPE)
        az_ds_out =  destroy.stdout.decode("utf-8")
        az_ds_err =  destroy.stderr.decode("utf-8")
        return az_ds_out
    except:
        return az_ds_err


def az_as_destroy(resource_group,as_name):
    try:
        az_destroy= "az vm availability-set delete --resource-group " + resource_group + " --name " + as_name
        print(az_destroy)
        destroy = subprocess.run(az_destroy, shell = True, stdout=subprocess.PIPE, stderr = subprocess.PIPE)
        az_ds_out =  destroy.stdout.decode("utf-8")
        az_ds_err =  destroy.stderr.decode("utf-8")
        return az_ds_out
    except:
        return az_ds_err


def ssh_connect(host,port,username,password):
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh_id=ssh.connect(host, port, username, password)
        return ssh;
    except:
        return False

        
def exec_shell_cmd(ssh_id,command_lst,log_file):
    try:
        for cmd in command_lst:
            stdin, stdout, stderr = ssh_id.exec_command(cmd)
            lines = stdout.readlines()
            for l in lines: 
                #print(l)
                with open(log_file, "a+",encoding='utf-8') as file: file.write(str(l))
        return True
    except:
        return False


def vfy_nginx(url,cond_chk):
    try:
        if "http" not in url:
            url="http://"+url
        data = urllib.request.urlopen(url).read()
        #print(data)
        bsoup = BeautifulSoup(data, "html.parser")
        title = bsoup.find('title')
        print(title)
        if cond_chk in title.string:
            return True
        else:
            return False
    except:
        return False


def get_ip(info):
    try:
        for line in info.split("\n"):
            ip = re.findall( r'[0-9]+(?:\.[0-9]+){3}', line )
            if ip:
                return ip
    except:
        return False    


def az_create_metric_alert(resource_group,vm_name,alert_name):
    try:
        az_scope="az vm show --resource-group "+ resource_group + " --name " + vm_name + " --output tsv --query id"
        az_condition="az monitor metrics alert condition create --aggregation Average --metric " + '"Percentage CPU"'  + " --op GreaterThan --type static --threshold 90 --output tsv"
        scope=subprocess.run(az_scope, shell = True, stdout=subprocess.PIPE, stderr = subprocess.PIPE)
        create_cond= subprocess.run(az_condition, shell = True, stdout=subprocess.PIPE, stderr = subprocess.PIPE)
        scope_op = scope.stdout.decode("utf-8").strip()
        cond_op= create_cond.stdout.decode("utf-8").strip()
        az_alert= "az monitor metrics alert create --name " + alert_name + " --resource-group " + resource_group + " --scopes " + scope_op.strip() + " --condition \"" + cond_op.strip() + "\" --description " + '"Test High CPU"'
        alert=subprocess.run(az_alert, shell = True, stdout=subprocess.PIPE, stderr = subprocess.PIPE)
        az_ale_out =  alert.stdout.decode("utf-8")
        az_ale_err =  alert.stderr.decode("utf-8")
        return az_ale_out
    except:
        return az_ale_err


def az_get_metric_alert(resource_group,alert_name):
    try:
        az_alert= "az monitor metrics alert show --name " + alert_name + " --resource-group " + resource_group
        get_alert=subprocess.run(az_alert, shell = True, stdout=subprocess.PIPE, stderr = subprocess.PIPE)
        az_ale_out =  get_alert.stdout.decode("utf-8")
        az_ale_err =  get_alert.stderr.decode("utf-8")
        return az_ale_out
    except:
        return az_ale_err


def az_delete_metric_alert(resource_group,alert_name):
    try:
        az_alert= "az monitor metrics alert delete --name " + alert_name + " --resource-group " + resource_group
        get_alert=subprocess.run(az_alert, shell = True, stdout=subprocess.PIPE, stderr = subprocess.PIPE)
        az_ale_out =  get_alert.stdout.decode("utf-8")
        az_ale_err =  get_alert.stderr.decode("utf-8")
        print(az_ale_out)
        return az_ale_out
    except:
        return az_ale_err
