"""Python library for configuring and testing distributed cloud features."""

import requests
import os
import json
from requests.structures import CaseInsensitiveDict


# path section
lib_path = os.path.dirname(__file__)
parent_folder_path = os.path.dirname(lib_path)
data_folder_path = os.path.join(parent_folder_path, "data/")
tests_folder_path = os.path.join(parent_folder_path, "tests/")

# endpoint urls section
baseurl = ".console.ves.volterra.io/api"
config_url = baseurl + "/config/"
ns_endpoint = baseurl+"/web/namespaces"
waf_endpoint = baseurl + "/waf"
k8s_endpoint = baseurl + "/vk8s"

# headers section
if os.getenv("APIToken"):
    token = os.getenv("APIToken")
else:
    token = "sample"
headers = CaseInsensitiveDict()
headers["Accept"] = "application/json"
headers["Authorization"] = "APIToken " + token


def get_all_namespaces(tenant="treino"):
    """Get all existing namespaces in a tenant"""
    ns_url = "https://" + tenant + ns_endpoint
    ns_resp = requests.get(ns_url, headers=headers)
    if ns_resp.status_code == 200:
        return ns_resp.json()
    else:
        raise Exception("APIToken is not working. Make sure this is latest and not expired.")


def validate_apitoken(tenant):
    """Validate if provided token is working."""
    ns_details = get_all_namespaces(tenant=tenant)
    if 'items' in ns_details.keys():
        print("Token is valid and working.")
    else:
        raise Exception("APIToken is not working. Make sure this is latest and not expired.")


def get_namespace(nsname="default", tenant="treino"):
    """Get a existing namespace in a tenant."""
    validate_apitoken(tenant=tenant)
    ns_url = "https://" + tenant + ns_endpoint + "/" + nsname
    ns_resp = requests.get(ns_url, headers=headers)
    if ns_resp.status_code == 200:
        return ns_resp.json()
    else:
        raise Exception("Please check the provided namespace.")


def get_all_app_firewalls(tenant="treino", namespace="default"):
    """Get all existing app firewalls in a namespace."""
    validate_apitoken(tenant=tenant)
    waf_url = "https://" + tenant + config_url + "namespaces/" + namespace + "/app_firewalls"
    waf_resp = requests.get(waf_url, headers=headers)
    if waf_resp.status_code == 200:
        return waf_resp.json()
    else:
        raise Exception("Please check the provided namespace name.")


def get_app_firewall(waf_name="default", namespace="default", tenant="treino"):
    """Get a specific app firewall details in a namespace."""
    validate_apitoken(tenant=tenant)
    waf_url = "https://" + tenant + config_url + "namespaces/" + namespace + "/app_firewalls/" + waf_name
    waf_resp = requests.get(waf_url, headers=headers)
    if waf_resp.status_code == 200:
        return waf_resp.json()
    else:
        raise Exception("Please check the provided namespace and firewall names.")


def update_app_firewall(new_spec_json_file, spec_data="", waf_name="fw", namespace="default", tenant="treino"):
    """Update a specific app firewall details in a namespace."""
    # validate APIToken
    validate_apitoken(tenant=tenant)

    # load and update data
    filepath = data_folder_path + new_spec_json_file
    json_data = json.loads(open(filepath, 'r').read())
    json_data['metadata']['name'] = waf_name
    json_data['metadata']['namespace'] = namespace
    if spec_data:
        json_data['spec'] = json.loads(spec_data)

    # send request
    waf_url = "https://" + tenant + config_url + "namespaces/" + namespace + "/app_firewalls/" + waf_name
    waf_resp = requests.put(waf_url, data=json.dumps(json_data), headers=headers)
    if waf_resp.status_code == 200:
        print("Application firewall: {0} updated successfully.".format(waf_name))
    else:
        raise Exception("Please check the provided input spec json file or data.")


def delete_app_firewall(waf_name, namespace="default", tenant="treino"):
    """Delete a specific app firewall in a namespace."""
    validate_apitoken(tenant=tenant)
    waf_url = "https://" + tenant + config_url + "namespaces/" + namespace + "/app_firewalls/" + waf_name
    waf_resp = requests.delete(waf_url, headers=headers)
    if waf_resp.status_code == 200:
        print("Application firewall: {0} deleted successfully.".format(waf_name))
    else:
        raise Exception("Please check the provided waf and namespace names.")


def get_http_loadbalancer(ns_name, lb_name, tenant="treino"):
    """Get HTTP load balancer details."""
    validate_apitoken(tenant=tenant)
    url = "https://{0}.console.ves.volterra.io/api/config/namespaces/{1}/http_loadbalancers/{2}".\
        format(tenant, ns_name, lb_name)
    lb_details = requests.get(url, headers=headers)
    if lb_details.status_code == 200:
        return lb_details.json()
    else:
        raise Exception("Please check the provided namespace and load balancer names.")


def delete_http_loadbalancer(ns_name, lb_name, tenant="treino"):
    """Delete HTTP load balancer details."""
    validate_apitoken(tenant=tenant)
    url = "https://{0}.console.ves.volterra.io/api/config/namespaces/{1}/http_loadbalancers/{2}".\
        format(tenant, ns_name, lb_name)
    lb_details = requests.delete(url, headers=headers)
    if lb_details.status_code == 200:
        return lb_details.json()
    else:
        raise Exception("Please check the provided namespace and load balancer names.")


def update_http_loadbalancer(ns_name, lb_name, json_file=None, json_data=None, tenant="treino"):
    """Update HTTP load balancer details."""
    validate_apitoken(tenant=tenant)
    url = "https://{0}.console.ves.volterra.io/api/config/namespaces/{1}/http_loadbalancers/{2}".\
        format(tenant, ns_name, lb_name)

    # load and update data
    if json_file:
        filepath = data_folder_path + json_file
        json_data = json.loads(open(filepath, 'r').read())
    elif not json_data:
        raise Exception("Please provide atleast one json input either file or data.")
    lb_details = requests.put(url, data=json.dumps(json_data), headers=headers)
    if lb_details.status_code == 200:
        print("Load balancer {0} updated successfully.".format(lb_name))
    else:
        raise Exception("Please check the provided load balancer data.")


def disable_ratelimiting(ns_name, lb_name):
    """Disable rate limiting feature on load balancer."""
    file_name = "f5xc_lb.json"
    update_http_loadbalancer(ns_name, lb_name, json_file=file_name)


def enable_ratelimiting(ns_name, lb_name, rate_limit_data=None):
    """Enable rate limiting feature on load balancer."""
    file_name = "f5xc_lb.json"
    filepath = data_folder_path + file_name
    json_data = json.loads(open(filepath, 'r').read())
    del json_data['spec']['disable_rate_limit']
    if rate_limit_data:
        json_data['spec']['rate_limit'] = rate_limit_data
    else:
        json_data['spec']['rate_limit'] = {
            "rate_limiter": {
                "total_number": 1,
                "unit": "SECOND",
                "burst_multiplier": 1
            },
            "no_ip_allowed_list": {},
            "no_policies": {}
        }
    update_http_loadbalancer(ns_name, lb_name, json_data=json_data)


def get_all_ratelimiters(ns_name, tenant="treino"):
    """Get all rate limiter details in a namespace."""
    validate_apitoken(tenant=tenant)
    url = "https://{0}.console.ves.volterra.io/api/config/namespaces/{1}/rate_limiters".format(tenant, ns_name)
    limiter_details = requests.get(url, headers=headers)
    if limiter_details.status_code == 200:
        return limiter_details.json()['items']
    else:
        raise Exception("Please check the provided namespace name.")


def create_ratelimiter(ns_name, tenant="treino"):
    """Create rate limiter in a namespace."""
    validate_apitoken(tenant=tenant)
    url = "https://{0}.console.ves.volterra.io/api/config/namespaces/{1}/rate_limiters".format(tenant, ns_name)

    # load and update data
    filepath = data_folder_path + "f5xc_ratelimiter.json"
    json_data = json.loads(open(filepath, 'r').read())

    # create rate limiter
    limiter_details = requests.post(url, data=json.dumps(json_data), headers=headers)
    if limiter_details.status_code == 200:
        return limiter_details.json()
    else:
        raise Exception("Unable to create rate limiter, please check the name.")


def delete_ratelimiter(ns_name, limiter_name, tenant="treino"):
    """Delete rate limiter in a namespace."""
    validate_apitoken(tenant=tenant)
    url = "https://{0}.console.ves.volterra.io/api/config/namespaces/{1}/rate_limiters/{2}".\
        format(tenant, ns_name, limiter_name)
    limiter_details = requests.delete(url, headers=headers)
    if limiter_details.status_code == 200:
        return limiter_details.json()
    else:
        raise Exception("Please check the provided namespace and rate limiter name.")


def get_ratelimiter(ns_name, limiter_name, tenant="treino"):
    """Get rate limiter details in a namespace."""
    validate_apitoken(tenant=tenant)
    url = "https://{0}.console.ves.volterra.io/api/config/namespaces/{1}/rate_limiters/{2}".\
        format(tenant, ns_name, limiter_name)
    limiter_details = requests.get(url, headers=headers)
    if limiter_details.status_code == 200:
        return limiter_details.json()
    else:
        raise Exception("Please check the provided namespace and rate limiter name.")


def create_ratelimiter_policy(ns_name, tenant="treino"):
    """Create rate limiter policy in a namespace."""
    validate_apitoken(tenant=tenant)
    url = "https://{0}.console.ves.volterra.io/api/config/namespaces/{1}/rate_limiter_policys".format(tenant, ns_name)

    # load and update data
    filepath = data_folder_path + "f5xc_ratelimiter_policy.json"
    json_data = json.loads(open(filepath, 'r').read())

    # create rate limiter
    limiter_details = requests.post(url, data=json.dumps(json_data), headers=headers)
    if limiter_details.status_code == 200:
        return limiter_details.json()
    else:
        raise Exception("Unable to create rate limiter policy, please check the name.")


def delete_ratelimiter_policy(ns_name, policy_name, tenant="treino"):
    """Delete rate limit policy in a namespace."""
    validate_apitoken(tenant=tenant)
    url = "https://{0}.console.ves.volterra.io/api/config/namespaces/{1}/rate_limiter_policys/{2}".\
        format(tenant, ns_name, policy_name)
    limiter_details = requests.delete(url, headers=headers)
    if limiter_details.status_code == 200:
        print("Rate limit policy {0} deleted successfully.".format(policy_name))
    else:
        raise Exception("Please check the provided namespace and rate limiter policy name.")


def get_ratelimiter_policy(ns_name, policy_name, tenant="treino"):
    """Get rate limit policy details in a namespace."""
    validate_apitoken(tenant=tenant)
    url = "https://{0}.console.ves.volterra.io/api/config/namespaces/{1}/rate_limiter_policys/{2}".\
        format(tenant, ns_name, policy_name)
    limiter_details = requests.get(url, headers=headers)
    if limiter_details.status_code == 200:
        return limiter_details.json()
    else:
        raise Exception("Please check the provided namespace and rate limiter policy name.")
