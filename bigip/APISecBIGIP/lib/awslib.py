import boto3,os
import time
from botocore.exceptions import ClientError
import paramiko
from scp import SCPClient
import re

def create_instance(sg_name, instance_name, image_name, key_pair, max_count, instance_type):
    """Lib to create AWS EC2 instance as per provided params."""
    ec = boto3.resource('ec2')
    try:
        sgid = get_security_group_id(sg_name)
        if not sgid:
            raise ValueError('Cannot create security group.')
        if "*" in image_name:
            imageid = get_image_id(image_name[:-1])
        else:
            imageid = get_image_id(image_name)
        if not imageid:
            raise ValueError('Unable to find image ID with this name: ' + image_name)
        ret = create_kpair(key_pair)
        print(ret)
        user_data = '''#!/bin/bash
        sudo apt -y update
        sudo apt -y install docker.io
        sudo apt -y install jq
        sudo sysctl -w vm.max_map_count=262144
        sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
        sudo chmod +x /usr/local/bin/docker-compose'''
        instances = ec.create_instances(
            ImageId=imageid,
            MinCount=1,
            MaxCount=max_count,
            InstanceType=instance_type,
            KeyName=key_pair,
            SecurityGroupIds=[sgid],
            UserData=user_data,
            BlockDeviceMappings=[
                {
                    'DeviceName': '/dev/sda1',
                    'Ebs': {
                        'DeleteOnTermination': True,
                        'VolumeSize': 20,
                        'VolumeType': 'gp2'
                        }
                }
            ]
        )
        ins_id = instances[0].instance_id
        if not ins_id:
            raise Exception('Unable to create instance.')
        ec.create_tags(Resources=[ins_id], Tags=[
            {
                'Key': 'Name',
                'Value': instance_name,
            },
        ])
        instances[0].wait_until_running()
        return ins_id
    except Exception as e:
        raise Exception(e)


def get_security_group_id(sg_name):
    """Create/Return security group ID by name."""
    ec2 = boto3.client('ec2')
    sg_count = 0
    for sg in ec2.describe_security_groups()["SecurityGroups"]:
        sg_count += 1
    sg = ec2.describe_security_groups()
    for itr_name in range(0, sg_count):
        name = sg.get('SecurityGroups', [{}])[itr_name].get('GroupName', '')
        if sg_name == name:
            sg_id = sg.get('SecurityGroups', [{}])[itr_name].get('GroupId', '')
            return sg_id
    vpcid = get_default_vpc()
    print("Default VPC ID:" + vpcid)
    try:
        sg = ec2.create_security_group(GroupName=sg_name, Description='sg through automation', VpcId=vpcid)
        sg_id = sg['GroupId']
        ec2.authorize_security_group_ingress(
            GroupId=sg_id,
            IpPermissions=[
                {'IpProtocol': 'tcp',
                 'FromPort': 80,
                 'ToPort': 80,
                 'IpRanges': [{'CidrIp': '0.0.0.0/0'}]},
                {'IpProtocol': 'tcp',
                 'FromPort': 443,
                 'ToPort': 443,
                 'IpRanges': [{'CidrIp': '0.0.0.0/0'}]},
                {'IpProtocol': 'tcp',
                 'FromPort': 22,
                 'ToPort': 22,
                 'IpRanges': [{'CidrIp': '0.0.0.0/0'}]},
                {'IpProtocol': 'tcp',
                 'FromPort': 5601,
                 'ToPort': 5601,
                 'IpRanges': [{'CidrIp': '0.0.0.0/0'}]},
                {'IpProtocol': 'tcp',
                 'FromPort': 5144,
                 'ToPort': 5144,
                 'IpRanges': [{'CidrIp': '0.0.0.0/0'}]},
                {'IpProtocol': 'tcp',
                 'FromPort': 9200,
                 'ToPort': 9200,
                 'IpRanges': [{'CidrIp': '0.0.0.0/0'}]}
            ])
        return sg_id
    except ClientError:
        raise Exception("Unable to get/update security group.")


def get_default_vpc():
    """Get default VPC ID."""
    ec2 = boto3.client('ec2')
    vpc_count = 0
    for vpc in ec2.describe_vpcs()["Vpcs"]:
        vpc_count += 1
    vpc = ec2.describe_vpcs()
    for vpcs in range(0, vpc_count):
        check = vpc.get('Vpcs', [{}])[vpcs].get('IsDefault', '')
        if check:
            vpc_id = vpc.get('Vpcs', [{}])[vpcs].get('VpcId', '')
            return vpc_id


def get_image_id(image_name):
    """Get AMI ID by AMI name."""
    ec2 = boto3.client('ec2')
    mkt_place = ec2.describe_images(Owners=['aws-marketplace'])
    cnt = 0
    for image in mkt_place['Images']:
        if image_name in mkt_place['Images'][cnt]['Name']:
            return mkt_place['Images'][cnt]['ImageId']
        cnt += 1
    raise Exception('=======image not found, kindly subscribe NAP image========')


def create_kpair(kname):
    """Create/Return key pair."""
    ec2 = boto3.client('ec2')
    list_keys = ec2.describe_key_pairs()
    for i in range(0, len(list_keys['KeyPairs'])):
        if list_keys['KeyPairs'][i]['KeyName'] == kname:
            print("========== Deleting key and recreating key with name: {}.pem  ==============".format(kname))
            del_kpair(kname)
    pemfile = open(kname + '.pem', 'w')
    key = ec2.create_key_pair(KeyName=kname)
    pemfile.write(key['KeyMaterial'])
    pemfile.close()
    return 'key created with name: ' + kname


def terminate_ec2(instance_id):
    """Terminate EC2 instance by ID."""
    ec2 = boto3.client('ec2')
    ec2.terminate_instances(InstanceIds=list(instance_id))
    time.sleep(10)
    return "successfully terminated ec2 instance!"


def del_kpair(key_name):
    os.environ['AWS_DEFAULT_REGION'] = 'ap-south-1'
    """Delete key value pair."""
    ec2 = boto3.client('ec2')
    ec2.delete_key_pair(KeyName=key_name)
    time.sleep(20)
    return "successfully deleted key pair from aws!"


def del_sg(sg_name):
    """Delete security group by name."""
    ec2 = boto3.client('ec2')
    ec2.delete_security_group(GroupName=sg_name)
    time.sleep(5)
    return "successfully initiated deletion of security group from aws!"


def fetch_public_ip(instance_name, instance_id):
    """Get public IP by name and ID."""
    ec2 = boto3.client('ec2')
    for i in ec2.describe_instances()['Reservations']:
        for j in i['Instances']:
            if j['InstanceId'] == instance_id:
                for k in j['Tags']:
                    if instance_name == k['Value']:
                        return j['PublicIpAddress']
    raise Exception('Public IP not found!')


def fetch_private_ip(instance_name, instance_id):
    """Get private IP by name and ID."""
    ec2 = boto3.client('ec2')
    for i in ec2.describe_instances()['Reservations']:
        for j in i['Instances']:
            if j['InstanceId'] == instance_id:
                for k in j['Tags']:
                    if instance_name == k['Value']:
                        return j['PrivateIpAddress']
    raise Exception('Private IP not found!')


def start_nginx(key_value, instance_name, instance_id, filename="NginxDefaultPolicy.json", pem_file=True):
    """Configure and start nginx using key pair and instance name."""
    if pem_file:
        key = paramiko.RSAKey.from_private_key_file("./" + key_value + ".pem")
    else:
        key = paramiko.RSAKey.from_private_key_file("./" + key_value)
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    pub_ip = fetch_public_ip(instance_name, str(instance_id))
    if pub_ip == 'not found!':
        raise ValueError('Unable to find public IP for NGINX instance.')
    pri_ip = fetch_private_ip(instance_name, str(instance_id))
    if pri_ip == 'not found!':
        raise ValueError('Unable to find private IP for NGINX instance.')
    try:
        client.connect(hostname=pub_ip, username="ubuntu", pkey=key)
        client.exec_command('sudo mv /etc/nginx/nginx.conf /etc/nginx/nginx_bkp.conf')
        scp = SCPClient(client.get_transport())
        scp.put(r'nginx.conf', '/home/ubuntu')
        print("====================== Copying files to instance. ========================")
        #modify_file_path="/builds/api-security/apisecurity/scripts/"
        #nginx_path="/builds/api-security/apisecurity/data/"
        #scp.put(r'modify_nginx_conf.py', '/home/ubuntu')
        # depending on file name change script execution
        #scp.put(r'nginx.conf', '/home/ubuntu')
        #print("================ Updating nginx conf file with script. ===================")
        client.exec_command('sudo mv /home/ubuntu/nginx.conf /etc/nginx/nginx.conf')
        client.exec_command('sudo systemctl restart nginx')
        time.sleep(10)
        stdin, stdout, stderr = client.exec_command('sudo systemctl status nginx')
        out = stdout.readlines()
        print("nginx status:",out)        
        '''
        if filename == "NginxDefaultPolicy.json":
            print("Private IP of instance is : {0} ".format(pri_ip))
            client.exec_command('python3 /home/ubuntu/modify_nginx_conf.py ' + str(pri_ip))
        else:
            scp.put(r'nginx-waffler.conf', '/home/ubuntu')
            client.exec_command('python3 /home/ubuntu/modify_nginx_conf.py ' + str(filename))
        client.exec_command('sudo cp /home/ubuntu/nginx.conf /etc/nginx')
        print("================== Copied updated nginx conf file. =========================")
        time.sleep(5)
        stdin, stdout, stderr = client.exec_command('sudo nginx -v')
        stdin.flush()
        err = stderr.readlines()
        print("=====================================================================")
        print('nginx -v ===>' + str(err[0]))
        print("=====================================================================")
        
        #client.exec_command('sudo su')
        print("=================== Stopping NGINX service. ===================================")
        client.exec_command('sudo systemctl stop nginx')
        time.sleep(10)
        print("===================== Starting NGINX service. =================================")
        client.exec_command('sudo systemctl start nginx')
        time.sleep(20)
        stdin, stdout, stderr = client.exec_command('sudo systemctl status nginx')
        #time.sleep(10)
        #stdin.flush()
        #stdout.channel.recv_exit_status()
        out = stdout.readlines()
        print("nginx status:",out)
        itr = 0
        for i in out:
            output = re.search("running", str(out[itr]))
            if output is not None:
                print("================= NGINX is up and running. ===========================")
                return 'nginx configured successfully!'
            itr += 1
        raise Exception('Unable to start nginx.')
        '''
        client.close()
    except Exception as e:
        raise Exception(e)


def find_dns(lb_name):
    """Get dns name for lb."""
    elblist = boto3.client('elbv2')
    elb = elblist.describe_load_balancers()
    for alb in elb['LoadBalancers']:
        if alb['LoadBalancerName'] == lb_name:
            return alb['DNSName']
    raise Exception("LB not found!")

