from ansible.module_utils.basic import AnsibleModule
import requests
import time

class CMOps:
    def __init__(self, cm_url, username, password, logger, timeout):
        self.cm_url = cm_url
        self.username = username
        self.password = password
        self.access_token = None
        self.logger = logger
        self.timeout = timeout
        self.login()

    def login(self):
        login_url = f"https://{self.cm_url}/api/login"
        headers = {"Content-Type": "application/json"}
        body = {"username": self.username, "password": self.password}

        response = requests.post(login_url, json=body, headers=headers, verify=False)
        response.raise_for_status()
        self.access_token = response.json().get("access_token")

    def poll_status(self, task_url):
        status_url = f"https://{self.cm_url}{task_url}"
        headers = {"Authorization": f"Bearer {self.access_token}", "Content-Type": "application/json"}

        for _ in range(self.timeout * 12): # check every 5 seconds -> 12 times a minute
            response = requests.get(status_url, headers=headers, verify=False)
            if response.status_code == 401:  # Token expired, need to re-login
                self.login()
                headers["Authorization"] = f"Bearer {self.access_token}"
                continue

            response.raise_for_status()
            response_json = response.json()

            status = response_json.get("status")
            id = response_json.get("id")
            name = response_json.get("name")

            self.logger('Task Polling: ' + id + ' - ' + name + ' > ' + status)

            failure_reason = response_json.get("failure_reason", "")
            if len(failure_reason) > 0:
                self.logger("Failure reason:" + id + " - " + failure_reason)

            if status == "completed":
                return {"success": True, "data": response_json }
            if status == "failed":
                return {"success": False, "data": response_json }
            time.sleep(5)
        return {"success": False, "data":{"failure_reason": "Deployment timed out"}}

    def deploy(self, policy_name, comment):
        deploy_url = f'https://{self.cm_url}/api/waf/v1/tasks/deploy-policy'
        headers = {
            'Authorization': f'Bearer {self.access_token}',
            'Content-Type': 'application/json'
        }
        deploy_body = {
            'comment': comment,
            'policy_name': policy_name
        }

        try:
            deploy_response = requests.post(
                deploy_url,
                json=deploy_body,
                headers=headers,
                verify=False
            )
            deploy_response.raise_for_status()
        except requests.exceptions.RequestException as e:
            module.fail_json(msg=f"Failed to initiate deployment: {e}")

        try:
            task_href = deploy_response.json()['_links']['self']['href']
            return task_href
        except (KeyError, TypeError) as e:
            module.fail_json(msg=f"Failed to parse deployment response: {e}")

def run_module():
    module_args = dict(
        cm_url=dict(type='str', required=True),
        username=dict(type='str', required=True),
        password=dict(type='str', required=True),
        policy_name=dict(type='str', required=True),
        comment=dict(type='str', required=True),
        timeout=dict(type='int', required=True)
    )

    result = dict(
        changed=False,
        message=''
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    cm_url = module.params['cm_url']
    username = module.params['username']
    password = module.params['password']
    policy_name = module.params['policy_name']
    comment = module.params['comment']
    timeout = module.params['timeout']

    def custom_logger(msg):
        with open('../logs/cm_polling.log', 'a') as f:
            f.write(f"{msg}\n")

    try:
        cm = CMOps(cm_url, username, password, custom_logger, timeout)
        task_url = cm.deploy(policy_name, comment)
        poll_result = cm.poll_status(task_url)
        if poll_result["success"]:
            result["success"] = True
            result['message'] = 'Live update status completed.'
            result['data'] = poll_result['data']
        else:
            result['message'] = poll_result['data']['failure_reason']
            result['success'] =  True
            module.fail_json(msg='Polling timed out.', **result)
    except Exception as e:
        module.fail_json(msg=f'Error: {str(e)}', **result)

    module.exit_json(**result)

def main():
    run_module()

if __name__ == '__main__':
    main()
