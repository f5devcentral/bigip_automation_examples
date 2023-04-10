"""Test all types of attacks provided in https://devcentral.f5.com/s/articles/
Declarative-Advanced-WAF-policy-lifecycle-in-a-CI-CD-pipeline."""

import os
import pytest
import graphqllib

cwd = os.getcwd()
bigip_file_path = cwd + "/bigip_public_ip"
user = "admin"
password = os.getenv("TF_VAR_F5_PASSWORD")


@pytest.fixture(scope="module")
def get_pubip():
    """Get public IP for BIG-IP component."""
    file_hand = open(bigip_file_path, 'r')
    pub_dns = file_hand.read()[0:-1]
    yield pub_dns


def test_verify_introspection(get_pubip):
    """Test introspection query."""
    pub_ip = get_pubip
    output = graphqllib.introspection_query(pub_ip, secure=True)
    if "support ID" in output:
        print("=============================  Introspection is blocked.  ============================")
    else:
        assert "data" in output, "Unknown text returned"
        print("=============================  Introspection is enabled.  ============================")


def test_cross_script_attack(get_pubip):
    """Test cross script attack."""
    pub_ip = get_pubip
    output = graphqllib.cross_script_attack(pub_ip, secure=True)
    if "support ID" in output:
        print("=============================  cross script attack blocked successfully.  ============================")
    else:
        assert "data" in output, "Unknown text returned"
        print("=============================  Unable to block XSS.  ============================")


def test_sql_inj_attack(get_pubip):
    """Test sql-injection attack."""
    pub_ip = get_pubip
    output = graphqllib.sql_injection_attack(pub_ip, secure=True)
    if "support ID" in output:
        print("=============================  sql-injection attack blocked successfully.  ============================")
    else:
        assert "data" in output, "Unknown text returned"
        print("=============================  Unable to block sql-injection.  ============================")


def test_command_inj_attack(get_pubip):
    """Test command-injection attack."""
    pub_ip = get_pubip
    output = graphqllib.command_execution_attack(pub_ip, secure=True)
    if "support ID" in output:
        print(
            "===========================  command-injection attack blocked successfully.  ==========================")
    else:
        assert "data" in output, "Unknown text returned"
        print("=============================  Unable to block command-injection.  ============================")


def test_dir_trav_attack(get_pubip):
    """Test dir-traversal attack."""
    pub_ip = get_pubip
    output = graphqllib.directory_traversal_attack(pub_ip, secure=True)
    if "support ID" in output:
        print("=============================  dir-traversal attack blocked successfully.  ============================")
    else:
        assert "data" in output, "Unknown text returned"
        print("=============================  Unable to block dir-traversal.  ============================")


def test_rec_qry_attack(get_pubip):
    """Test recursive query attack."""
    pub_ip = get_pubip
    output = graphqllib.recursive_query_attack(pub_ip, secure=True)
    if "support ID" in output:
        print(
            "=============================  recursive query attack blocked successfully.  ============================")
    else:
        assert "Cannot query field" in output, "Unknown text returned"
        print("=============================  Unable to block recursive-query.  ============================")


def test_get_info(get_pubip):
    """get info of specific field."""
    pub_ip = get_pubip
    output = graphqllib.get_info(pub_ip, secure=True)
    if "support ID" in output:
        print("=============================  Unable to fetch details of application.  ============================")
    else:
        assert "data" in output, "Unknown text returned"
        print("=============================  Able to fetch info.  ============================")


def test_malformed_req(get_pubip):
    """test malformed query."""
    pub_ip = get_pubip
    output = graphqllib.malformed_req(pub_ip, secure=True)
    if "support ID" in output:
        print("=============================  malformed req blocked.  ============================")
    else:
        assert "groupID" in output, "Unknown text returned"
        print("=============================  Unable to block malformed req.  ============================")
