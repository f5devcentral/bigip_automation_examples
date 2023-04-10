"""Test rate limiting feature provided in
https://community.f5.com/t5/technical-articles/introduction-to-f5-distributed-cloud-console-rate-limiting/ta-p/293606"""


import pytest
import requests
import json

var_file_data = json.loads(open("terraform.tfvars.json", 'r').read())
pub_dns = var_file_data["domain_name"]
pub_dns_url = "http://"+pub_dns


@pytest.fixture(scope="module")
def get_pubip():
    """Get load balancer domain name."""
    yield pub_dns_url


def test_application_ratelimit(get_pubip):
    """Validate if rate limiting is blocking requests successfully."""
    pub_ip = get_pubip
    blocked = False
    for iteration in range(3):
        print("Sending request no: "+str(iteration)+" to application at "+str(pub_dns_url))
        out = requests.get(pub_ip)
        if out.status_code == 429:
            blocked = True
            break
    assert blocked
    print("=================================  Application is blocked by rate limiting.  "
          "====================================")
