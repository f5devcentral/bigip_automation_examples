"""BigIP library functions."""

import requests
from requests.auth import HTTPBasicAuth
import json

headers = {'Content-type': 'application/json'}


def get_asm_policies(bigip, username, password):
    """Get all ASM policies."""
    url = "https://" + bigip + ":8443/mgmt/tm/asm/policies?$select=name,id"
    resp = requests.get(url, auth=HTTPBasicAuth(username, password), verify=False)
    if resp.status_code != 200:
        return "Unable to get ASM policies, please check URL, username and passwords."
    return resp.text


def export_learnings(bigip, username, password, policy_id):
    """Export all learning suggestions."""
    url = "https://" + bigip + ":8443/mgmt/tm/asm/tasks/export-suggestions"
    data = {
        "inline": "true",
        "policyReference": {
                "link": "https://localhost/mgmt/tm/asm/policies/" + str(policy_id)
            }
    }
    resp = requests.post(url, auth=HTTPBasicAuth(username, password), data=json.dumps(data), verify=False)
    if resp.status_code != 201:
        return "Unable to export learning suggestions, please check URL, username and passwords."
    return resp.text


def get_learning_suggestions(bigip, username, password):
    """Get all learning suggestions."""
    url = "https://" + bigip + ":8443/mgmt/tm/asm/tasks/export-suggestions"
    resp = requests.get(url, auth=HTTPBasicAuth(username, password), verify=False)
    if resp.status_code != 200:
        return "Unable to get learning suggestions, please check URL, username and passwords."
    return resp.text
