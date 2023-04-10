import json
import os
import pytest
import attackslib
import arcadialib
import bigiplib
import time


cwd = os.getcwd()
print("cwd:",cwd)
bigip_file_path = cwd + "/bigip_public_dns"
user = "admin"
password = "f5root021"
#password = os.getenv("TF_VAR_F5_PASSWORD")


@pytest.fixture(scope="module")
def get_pubip():
    """Get public IP for BIG-IP component."""
    file_hand = open(bigip_file_path, 'r')
    pub_dns = file_hand.read()
    yield pub_dns


def test_application(get_pubip):
    """Validate if application is running successfully."""
    pub_ip = get_pubip
    print("pub_ip",pub_ip)
    out = arcadialib.check_arcadia(pub_ip, secure=True)
    assert "successfully" in out
    print("=================================  Arcadia application is running.  ====================================")


def test_cross_script_attack(get_pubip):
    """Test cross script attack."""
    pub_ip = get_pubip
    output = attackslib.cross_script_attack(pub_ip, secure=True)
    assert "support ID" in output
    print("=============================  cross script attack blocked successfully.  ============================")


def test_cross_script_attack_url(get_pubip):
    """Test cross script attack with url."""
    pub_ip = get_pubip
    output = attackslib.cross_script_attack_url(pub_ip, secure=True)
    assert "support ID" in output
    print("=============================  cross script attack blocked successfully.  ============================")


def test_cross_script_attack_header(get_pubip):
    """Test cross script attack with header."""
    pub_ip = get_pubip
    output = attackslib.cross_script_attack_header(pub_ip, secure=True)
    assert "support ID" in output
    print("=============================  cross script attack blocked successfully.  ============================")


def test_cross_script_attack_mouse_over_url(get_pubip):
    """Test cross script attack with url."""
    pub_ip = get_pubip
    output = attackslib.cross_script_attack_mouse_over_url(pub_ip, secure=True)
    assert "support ID" in output
    print("=============================  cross script attack blocked successfully.  ============================")


def test_cross_script_attack_mouse_over_headers(get_pubip):
    """Test cross script attack with headers."""
    pub_ip = get_pubip
    output = attackslib.cross_script_attack_mouse_over_headers(pub_ip, secure=True)
    assert "support ID" in output
    print("=============================  cross script attack blocked successfully.  ============================")


def test_cross_script_attack_eval_param(get_pubip):
    """Test cross script attack with param."""
    pub_ip = get_pubip
    output = attackslib.cross_script_attack_eval_param(pub_ip, secure=True)
    assert "support ID" in output
    print("=============================  cross script attack blocked successfully.  ============================")


def test_cross_script_attack_eval_headers(get_pubip):
    """Test cross script attack with headers."""
    pub_ip = get_pubip
    output = attackslib.cross_script_attack_eval_headers(pub_ip, secure=True)
    assert "support ID" in output
    print("==========================  cross script eval attack blocked successfully.  =========================")


def test_sql_injection_attack(get_pubip):
    """Test sql injection attack."""
    pub_ip = get_pubip
    output = attackslib.sql_injection_attack(pub_ip, secure=True)
    assert "support ID" in output
    print("==========================  sql injection attack blocked successfully.  ========================")


def test_sql_injection_attack_union_param(get_pubip):
    """Test sql injection attack."""
    pub_ip = get_pubip
    output = attackslib.sql_injection_attack_union_param(pub_ip, secure=True)
    assert "support ID" in output
    print("==========================  sql injection attack blocked successfully.  ========================")


def test_sql_injection_attack_union_url(get_pubip):
    """Test sql injection attack."""
    pub_ip = get_pubip
    output = attackslib.sql_injection_attack_union_url(pub_ip, secure=True)
    assert "support ID" in output
    print("==========================  sql injection attack blocked successfully.  ========================")


def test_sql_injection_attack_union_headers(get_pubip):
    """Test sql injection attack."""
    pub_ip = get_pubip
    output = attackslib.sql_injection_attack_union_headers(pub_ip, secure=True)
    assert "support ID" in output
    print("==========================  sql injection attack blocked successfully.  ========================")


def test_sql_injection_attack_blind_param(get_pubip):
    """Test sql injection attack."""
    pub_ip = get_pubip
    output = attackslib.sql_injection_attack_blind_param(pub_ip, secure=True)
    assert "support ID" in output
    print("==========================  sql injection attack blocked successfully.  ========================")


def test_sql_injection_attack_blind_url(get_pubip):
    """Test sql injection attack."""
    pub_ip = get_pubip
    output = attackslib.sql_injection_attack_blind_url(pub_ip, secure=True)
    assert "support ID" in output
    print("==========================  sql injection attack blocked successfully.  ========================")


def test_sql_injection_attack_blind_headers(get_pubip):
    """Test sql injection attack."""
    pub_ip = get_pubip
    output = attackslib.sql_injection_attack_blind_headers(pub_ip, secure=True)
    assert "support ID" in output
    print("==========================  sql injection attack blocked successfully.  ========================")


def test_nosql_injection_attack_param(get_pubip):
    """Test no sql injection attack."""
    pub_ip = get_pubip
    output = attackslib.nosql_injection_attack_param(pub_ip, secure=True)
    assert "support ID" in output
    print("==========================  no sql injection attack blocked successfully.  ========================")


def test_nosql_injection_attack_url(get_pubip):
    """Test no sql injection attack."""
    pub_ip = get_pubip
    output = attackslib.nosql_injection_attack_url(pub_ip, secure=True)
    assert "support ID" in output
    print("==========================  no sql injection attack blocked successfully.  ========================")


def test_nosql_injection_attack_headers(get_pubip):
    """Test no sql injection attack."""
    pub_ip = get_pubip
    output = attackslib.nosql_injection_attack_headers(pub_ip, secure=True)
    assert "support ID" in output
    print("==========================  no sql injection attack blocked successfully.  ========================")


def test_command_injection_attack_header(get_pubip):
    """Test command injection attack."""
    pub_ip = get_pubip
    output = attackslib.command_injection_attack_header(pub_ip, secure=True)
    assert "support ID" in output
    print("==========================  command injection attack blocked successfully.  ========================")


def test_command_injection_attack_powershell_url(get_pubip):
    """Test command injection attack."""
    pub_ip = get_pubip
    output = attackslib.command_injection_attack_powershell_url(pub_ip, secure=True)
    assert "support ID" in output
    print("==========================  command injection attack blocked successfully.  ========================")


def test_command_injection_attack_powershell_param(get_pubip):
    """Test command injection attack."""
    pub_ip = get_pubip
    output = attackslib.command_injection_attack_powershell_param(pub_ip, secure=True)
    assert "support ID" in output
    print("==========================  command injection attack blocked successfully.  ========================")


def test_command_injection_attack_powershell_header(get_pubip):
    """Test command injection attack."""
    pub_ip = get_pubip
    output = attackslib.command_injection_attack_powershell_header(pub_ip, secure=True)
    assert "support ID" in output
    print("==========================  command injection attack blocked successfully.  ========================")


def test_directory_traversal_attack_header(get_pubip):
    """Test directory traversal attack."""
    pub_ip = get_pubip
    output = attackslib.directory_traversal_attack_header(pub_ip, secure=True)
    assert "support ID" in output
    print("==========================  directory traversal attack blocked successfully.  ========================")


def test_predictable_attack(get_pubip):
    """Test predictable traversal attack."""
    pub_ip = get_pubip
    output = attackslib.predictable_attack(pub_ip, secure=True)
    assert "support ID" in output
    print("==========================  predictable traversal attack blocked successfully.  ========================")


def test_compliance_attack(get_pubip):
    time.sleep(180)
    """Test compliance attack."""
    pub_ip = get_pubip
    output = attackslib.compliance_attack(pub_ip, secure=True)
    assert "support ID" in output
    print("==========================  compliance attack blocked successfully.  ========================")


def test_ssrf_attack_aws(get_pubip):
    """Test compliance attack."""
    pub_ip = get_pubip
    output = attackslib.ssrf_attack_aws(pub_ip, secure=True)
    assert "support ID" in output
    print("==========================  SSRF attack blocked successfully.  ========================")


def test_insecure_deserialization_attack_php_param(get_pubip):
    """Test command injection attack."""
    pub_ip = get_pubip
    output = attackslib.insecure_deserialization_attack_php_param(pub_ip, secure=True)
    assert "support ID" in output
    print("======================  command injection attack blocked successfully.  =============")


def test_insecure_deserialization_attack_php_url(get_pubip):
    """Test command injection attack."""
    pub_ip = get_pubip
    output = attackslib.insecure_deserialization_attack_php_url(pub_ip, secure=True)
    assert "support ID" in output
    print("======================  command injection attack blocked successfully.  =============")


def test_insecure_deserialization_attack_php_header(get_pubip):
    """Test command injection attack."""
    pub_ip = get_pubip
    output = attackslib.insecure_deserialization_attack_php_header(pub_ip, secure=True)
    assert "support ID" in output
    print("======================  command injection attack blocked successfully.  =============")


def test_xml_external_entity_attack(get_pubip):
    """Test xml external attack"""
    pub_ip = get_pubip
    output = attackslib.xml_external_entity(pub_ip, secure=True)
    assert "support ID" in output
    print("======================  xml attack blocked successfully.  =============")


def test_code_injection_attack(get_pubip):
    """Test code injection attack."""
    pub_ip = get_pubip
    output = attackslib.code_injection_attack(pub_ip, secure=True)
    assert "support ID" in output
    print("======================  code injection attack blocked successfully.  =============")


def test_csrf_attack(get_pubip):
    """Test csrf attack."""
    pub_ip = get_pubip
    output = attackslib.code_injection_attack(pub_ip, secure=True)
    assert "support ID" in output
    print("======================  CSRF attack blocked successfully.  =============")

def test_evasion_attack(get_pubip):
    """Test compliance attack."""
    pub_ip = get_pubip
    output = attackslib.evasion_attack(pub_ip, secure=True)
    assert "Arcadia Finance" in output


def test_buy_stocks(get_pubip):
    """Test buy stocks valid request."""
    pub_ip = get_pubip
    req = arcadialib.buy_stocks(pub_ip, "buy_stocks.json", secure=True)
    assert '"status":"success"' in req
    print("======================  Buy stocks API validated successfully.  =============")


def test_sell_stocks(get_pubip):
    """Test sell stocks valid request."""
    pub_ip = get_pubip
    req = arcadialib.sell_stocks(pub_ip, "sell_stocks.json", secure=True)
    assert '"status":"success"' in req
    print("======================  Sell stocks API validated successfully.  =============")


def test_transfer_money(get_pubip):
    """Test transfer money request."""
    pub_ip = get_pubip
    req = arcadialib.transfer_money(pub_ip, "transfer_money.json", secure=True)
    assert req.status_code == 200
    print("======================  Transfer money API validated successfully.  =============")


def test_last_transactions(get_pubip):
    """Test last transactions valid request."""
    pub_ip = get_pubip
    req = arcadialib.last_transactions(pub_ip, secure=True)
    assert 'Last Transactions' in req
    print("======================  Last transactions API validated successfully.  =============")


def test_get_learning_suggestions(get_pubip):
    """Validate learning suggestions."""
    pub_ip = get_pubip
    policies = bigiplib.get_asm_policies(pub_ip, user, password)
    policy_id = json.loads(policies)['items'][0]['id']
    bigiplib.export_learnings(pub_ip, user, password, policy_id)
    suggestions = bigiplib.get_learning_suggestions(pub_ip, user, password)
    assert suggestions
    print("======================  Learning suggestions validated successfully.  =============")
