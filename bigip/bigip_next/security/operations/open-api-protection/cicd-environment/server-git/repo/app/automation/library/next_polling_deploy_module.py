#!/usr/bin/python

from ansible.module_utils.basic import AnsibleModule
import requests
import time
from datetime import datetime

class NextDeployPolling:
    def __init__(self, next_url, username, password, logger, timeout):
        self.next_url = next_url
        self.username = username
        self.password = password
        self.access_token = None
        self.logger = logger
        self.timeout = timeout
        self.login()

    def login(self):
        login_url = f"https://{self.next_url}/api/login"
        headers = {"Content-Type": "application/json"}
        body = {"username": self.username, "password": self.password}

        response = requests.post(login_url, json=body, headers=headers, verify=False)
        response.raise_for_status()
        self.access_token = response.json().get("access_token")

    def poll_status(self, task_url):
        status_url = f"https://{self.next_url}{task_url}"
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
            policy_name = response_json.get("policies", [""])[0]

            current_datetime = datetime.now()
            formatted_datetime = current_datetime.strftime('%Y-%m-%dT%H-%M-%S')
            self.logger('[' + formatted_datetime + '] Task Polling: ' + id + ' - ' + name + " - " + policy_name + ' > ' + status)

            failure_reason = response_json.get("failure_reason", "")
            if len(failure_reason) > 0:
                self.logger('[' + formatted_datetime + '] Failure reason:' + id + ' - ' + failure_reason)

            if status == "completed":
                return {"success": True, "data": response.json()}
            time.sleep(5)
        return {"success": False}

def run_module():
    module_args = dict(
        next_url=dict(type='str', required=True),
        username=dict(type='str', required=True),
        password=dict(type='str', required=True),
        task_url=dict(type='str', required=True),
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

    next_url = module.params['next_url']
    username = module.params['username']
    password = module.params['password']
    task_url = module.params['task_url']
    timeout = module.params['timeout']

    def custom_logger(msg):
        with open('../logs_next_polling.log', 'a') as f:
            f.write(f"{msg}\n")

    try:
        process = NextDeployPolling(next_url, username, password, custom_logger, timeout)
        poll_result = process.poll_status(task_url)
        if poll_result["success"]:
            result["success"] = True
            result['message'] = 'Task status completed.'
            result['data'] = poll_result['data']
        else:
            result['message'] = 'Polling timed out.'
            result['success'] = False
            module.fail_json(msg='Polling timed out.', **result)
    except Exception as e:
        module.fail_json(msg=f'Error: {str(e)}', **result)

    module.exit_json(**result)

def main():
    run_module()

if __name__ == '__main__':
    main()


