"""Test XSS injection attack provided in https://owasp.org/Top10/"""

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


def test_xss_injection(get_pubip):
    """Validate if XSS request is blocked successfully."""
    pub_ip = get_pubip
    print("Sending XSS request to application.")
    out = requests.get(pub_ip+"?a=<script>")
    assert "The requested URL was rejected. Please consult with your administrator." in out.text
    print("=================================  Application is blocked by WAF.  ====================================")
