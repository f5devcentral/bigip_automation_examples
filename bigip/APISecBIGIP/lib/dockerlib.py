import paramiko
from scp import SCPClient
import time
import re
import json
import requests
import textwrap
import awslib

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
'''
def deploy_app(pub_ip, key_pair, username="ubuntu", pem_file=True):
    """Deploy application for EC2 instance with IP: pub_ip."""
    if pem_file:
        key = paramiko.RSAKey.from_private_key_file("./" + key_pair + ".pem")
    else:
        key = paramiko.RSAKey.from_private_key_file("./" + key_pair)
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        print("========================= Connecting to instance. =============================")
        client.connect(username=username, hostname=pub_ip, pkey=key)
        scp = SCPClient(client.get_transport())
        print("=============== Waiting for 5 mins to download all images. ====================")
        time.sleep(300)
        print("========================= Copying data to instance. ===========================")
        scp.put(r'/builds/api-security/apisecurity/data/default.conf', '/home/ubuntu')
        print("=============== Running docker commands to install app. =======================")
        client.exec_command('sudo docker network create internal')
        time.sleep(5)
        client.exec_command('sudo docker run -dit -h mainapp --name=mainapp --net=internal '
                            'registry.gitlab.com/arcadia-application/main-app/mainapp:latest')
        time.sleep(30)
        client.exec_command('sudo docker run -dit -h backend --name=backend --net=internal '
                            'registry.gitlab.com/arcadia-application/back-end/backend:latest')
        time.sleep(30)
        client.exec_command('sudo docker run -dit -h app2 --name=app2 --net=internal '
                            'registry.gitlab.com/arcadia-application/app2/app2:latest')
        time.sleep(30)
        client.exec_command('sudo docker run -dit -h app3 --name=app3 --net=internal '
                            'registry.gitlab.com/arcadia-application/app3/app3:latest')
        time.sleep(30)
        client.exec_command('sudo docker run -dit -h nginx --name=nginx --net=internal -p 8080:80 -v '
                            '/home/ubuntu/default.conf:/etc/nginx/conf.d/default.conf '
                            'registry.gitlab.com/arcadia-application/nginx/nginxoss:latest')
        time.sleep(50)
        stdin, stdout, stderr = client.exec_command('sudo docker ps -a')
        stdout.channel.recv_exit_status()
        ret = stdout.readlines()
        print("======================  Printing docker ps output  ===================")
        print(ret)
        print("======================================================================")
        itr = 0
        for i in ret:
            if re.search("Exited", str(ret[itr])):
                print("========================= Some containers are not up. ===========================")
                raise Exception('all containers are not running')
            itr += 1
        client.close()
        return 'app deployed successfully'
    except Exception as e:
        raise Exception(e)
'''
def deploy_app(pub_ip, key_pair, username="ubuntu", pem_file=True):
    """Deploy application for EC2 instance with IP: pub_ip."""
    #default_conf_path="/builds/api-security/apisecurity/data/default.conf"
    #nginx_conf_path=""
    if pem_file:
        key = paramiko.RSAKey.from_private_key_file("./" + key_pair + ".pem")
    else:
        key = paramiko.RSAKey.from_private_key_file("./" + key_pair)
    #if client:
    #    client.close()
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        print("========================= Connecting to instance. =============================")
        client.connect(username=username, hostname=pub_ip, pkey=key)
        client.exec_command('pwd')
        client.exec_command('ls')
        scp = SCPClient(client.get_transport())
        #client.close()
        
        scp.put(r'/root/actions-runner/sdc-runner/verified_designs_examples/verified_designs_examples/bigip/APISecBIGIP/data/default.conf', '/home/ubuntu')
        
        #print("=============== Waiting for 5 mins to download all images. ====================")
        #time.sleep(300)
        #print("========================= Copying data to instance. ===========================")
        #scp.put(r'/root/actions-runner/sdc-runner/apisecurity/apisecurity/tests/nap-deployment-aws-cloud/default.conf', '/home/ubuntu')
        #scp.put(r'default.conf', '/home/ubuntu')
        
        print("=============== Running docker commands to install app. =======================")
        client.exec_command('sudo docker network create internal')
        time.sleep(5)
        client.exec_command('sudo docker run -dit -h mainapp --name=mainapp --net=internal '
                            'registry.gitlab.com/arcadia-application/main-app/mainapp:latest')
        time.sleep(30)
        client.exec_command('sudo docker run -dit -h backend --name=backend --net=internal '
                            'registry.gitlab.com/arcadia-application/back-end/backend:latest')
        time.sleep(30)
        client.exec_command('sudo docker run -dit -h app2 --name=app2 --net=internal '
                            'registry.gitlab.com/arcadia-application/app2/app2:latest')
        time.sleep(30)
        client.exec_command('sudo docker run -dit -h app3 --name=app3 --net=internal '
                            'registry.gitlab.com/arcadia-application/app3/app3:latest')
        time.sleep(30)
        client.exec_command('sudo docker run -dit -h nginx --name=nginx --net=internal -p 8080:80 -v '
                            '/home/ubuntu/default.conf:/etc/nginx/conf.d/default.conf '
                            'registry.gitlab.com/arcadia-application/nginx/nginxoss:latest')
        time.sleep(50)
        stdin, stdout, stderr = client.exec_command('sudo docker ps -a')
        stdout.channel.recv_exit_status()
        ret = stdout.readlines()
        print("======================  Printing docker ps output  ===================")
        print(ret)
        print("======================================================================")
        itr = 0
        for i in ret:
            if re.search("Exited", str(ret[itr])):
                print("========================= Some containers are not up. ===========================")
                raise Exception('all containers are not running')
            itr += 1
        client.close()
        
        return 'app deployed successfully'
    except Exception as e:
        print(e)
        raise Exception(e)


def install_docker(key_pair, pub_ip, username="ubuntu"):
    "Lib to install and validate docker."
    key = paramiko.RSAKey.from_private_key_file("./" + key_pair + ".pem")
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        client.connect(username=username, hostname=pub_ip, pkey=key)
        client.exec_command('sudo su')
        time.sleep(30)
        print("=======executing nginx -v command===========")
        stdin, stdout, stderr = client.exec_command('sudo nginx -v')
        stdin.flush()
        err = stderr.readlines()
        print('nginx -v ===>' + str(err[0]))
        stdin, stdout, stderr = client.exec_command(r"sudo apt -y install docker.io")
        time.sleep(90)
        print("=============executed command to install docker ============")
        stdin, stdout, stderr = client.exec_command('sudo docker -v')
        stdin.flush()
        output = stdout.readlines()
        print(output)
        if not output:
            raise Exception('unable to install docker')
        return 'docker installed successfully!'
    except Exception as e:
        raise Exception(e)


def install_elk(key_pair, pub_ip, username="ubuntu"):
    """Lib to install elk in an instance."""
    key = paramiko.RSAKey.from_private_key_file("./" + key_pair + ".pem")
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        client.connect(username=username, hostname=pub_ip, pkey=key)
        client.exec_command('sudo git clone https://github.com/f5devcentral/f5-waf-elk-dashboards.git')
        time.sleep(20)
        client.exec_command('sudo cd ~')
        stdin, stdout, stderr = \
            client.exec_command(r'''sudo docker-compose -f f5-waf-elk-dashboards/docker-compose.yaml up -d''')
        print("========================= docker compose stdout print======================")
        print(stdout.readlines())
        print("========================= docker compose stderr print======================")
        print(stderr.readlines())
        time.sleep(300)
        client.connect(username=username, hostname=pub_ip, pkey=key)
        stdin, stdout, stderr = client.exec_command('sudo docker ps')
        stdin.flush()
        output = stdout.readlines()
        dashboard_cmd = textwrap.dedent("""
KIBANA_URL=http://localhost:5601
jq -s . /home/ubuntu/f5-waf-elk-dashboards/kibana/overview-dashboard.ndjson | jq '{"objects": . }' | \
curl -k --location --request POST "$KIBANA_URL/api/kibana/dashboards/import" \
    --header 'kbn-xsrf: true' \
    --header 'Content-Type: text/plain' -d @- \
    | jq
""")
        stdin, stdout, stderr = client.exec_command(dashboard_cmd)
        for cnt in output:
            if 'sebp/elk' in cnt:
                if "Up" in cnt:
                    return 'ELK installed successfully!'
        else:
            raise Exception('Unable to install ELK with docker compose.')
    except Exception as e:
        raise Exception(e)


def validate_elk_logs(pubip, index, log_type, filter, ssl_type="http", port=9200):
    """
    Get ELK logs either all or by filters.
    pubip: pubip for instance
    index: index name
    log_type: type of log ex: _doc, _json, etc
    filter: we can pass simple value to search in all fields or specific key and value
        Ex: filter can be string like "security", "12344", etc
        or we can also give like "name:jani" which will filter only for this key and value
    ssl_type: can be http or https
    port: elastic search port number. Default is 9200
    """
    url = "{0}://{1}:{2}/{3}/{4}/_search?q={5}".format(ssl_type, pubip, port, index, log_type, filter)
    output = requests.get(url)
    assert output.status_code == 200
    output_logs = json.loads(output.text)
    for output_log in output_logs['hits']['hits']:
        if ":" in filter:
            filter_elements = filter.split(":")
            assert output_log["_source"][filter_elements[0]] == filter_elements[1]
        else:
            assert filter in output_log["_source"].values()


def validate_nap_with_json(pub_ip, key_pair, filename, instancename, instanceid, username="ubuntu", pem_file=True):
    """This lib will copy json file and try to restart nginx."""
    if pem_file:
        key = paramiko.RSAKey.from_private_key_file("./" + key_pair + ".pem")
    else:
        key = paramiko.RSAKey.from_private_key_file("./" + key_pair)
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        print("========================= Connecting to instance. =============================")
        client.connect(username=username, hostname=pub_ip, pkey=key)
        print("Disabling SELINX temporarily..")
        client.exec_command('sudo setenforce 0')
        scp = SCPClient(client.get_transport())
        print("========================= Copying json data to instance. ===========================")
        scp.put(r'/builds/api-security/apisecurity/tests/waffler/chrome/'+filename, '/home/ubuntu')
        print("================= moving json data to app protect conf location. ===================")
        client.exec_command('sudo mv /home/ubuntu/waf-* /etc/app_protect/conf/')
        print("=============== Starting nginx with latest waf json file. ==========================")
        awslib.start_nginx(key_pair, instancename, instanceid, filename)
        print("===================== NGINX service is up with file: {0} ===========================".format(filename))
    except Exception as e:
        raise Exception(e)
