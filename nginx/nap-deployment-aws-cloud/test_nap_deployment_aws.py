"""Test all types of attacks provided in
https://devcentral.f5.com/s/articles/NGINX-App-Protect-Deployment-in-AWS-Cloud."""

import os
import pytest
import attackslib
import arcadialib


@pytest.fixture(scope="module")
def get_pubip():
    """Get public IP for ALB component."""
    cwd = os.getcwd()
    print("cwd:",cwd)
    alb_file_path = cwd + "/terraform/alb_dns"
    file_hand = open(alb_file_path, 'r')
    pub_dns = file_hand.read()
    yield pub_dns


def test_application(get_pubip):
    """Validate if application is running successfully."""
    pub_ip = get_pubip
    print("================================ ALB DNS is: {0} ===========================================".format(pub_ip))
    accessible = False
    # try few times and validate if arcadia is running
    for x in range(5):
        out = arcadialib.check_arcadia(pub_ip, secure=False)
        if "successfully" in out:
            accessible = True
            break
    assert accessible
    print("=================================  Arcadia application is running.  ====================================")


def test_cross_script_attack(get_pubip):
    """Test cross script attack."""
    pub_ip = get_pubip
    output = attackslib.cross_script_attack(pub_ip, secure=False)
    assert "support ID" in output
    print("=============================  cross script attack blocked successfully.  ============================")


def test_cross_script_attack_url(get_pubip):
    """Test cross script attack with url."""
    pub_ip = get_pubip
    output = attackslib.cross_script_attack_url(pub_ip, secure=False)
    assert "support ID" in output
    print("=============================  cross script attack blocked successfully.  ============================")


def test_cross_script_attack_mouse_over_url(get_pubip):
    """Test cross script attack with url."""
    pub_ip = get_pubip
    output = attackslib.cross_script_attack_mouse_over_url(pub_ip, secure=False)
    assert "support ID" in output
    print("=============================  cross script attack blocked successfully.  ============================")


def test_command_injection_attack(get_pubip):
    """Test command injection attack."""
    pub_ip = get_pubip
    output = attackslib.command_injection_attack(pub_ip)
    assert "support ID" in output
    print("================      command injection attack blocked. =================")


def test_command_injection_attack_powershell_url(get_pubip):
    """Test command injection attack."""
    pub_ip = get_pubip
    output = attackslib.command_injection_attack_powershell_url(pub_ip)
    assert "support ID" in output
    print("==========================  command injection attack blocked successfully.  ========================")


def test_command_injection_attack_powershell_param(get_pubip):
    """Test command injection attack."""
    pub_ip = get_pubip
    output = attackslib.command_injection_attack_powershell_param(pub_ip)
    assert "support ID" in output
    print("==========================  command injection attack blocked successfully.  ========================")


def test_directory_traversal_attack(get_pubip):
    """Test directory traversal attack."""
    pub_ip = get_pubip
    output = attackslib.directory_traversal_attack(pub_ip, secure=False)
    assert "support ID" in output
    print("==========================  directory traversal attack blocked successfully.  ========================")


def test_file_inclusion_attack(get_pubip):
    """Test file inclusion attack."""
    pub_ip = get_pubip
    output = attackslib.file_inclusion_attack(pub_ip, secure=False)
    assert "support ID" in output
    print("======================  file inclusion attack blocked successfully.  =============")


def test_code_injection_attack(get_pubip):
    """Test code injection attack."""
    pub_ip = get_pubip
    output = attackslib.code_injection_attack(pub_ip, secure=False)
    assert "support ID" in output
    print("======================  code injection attack blocked successfully.  =============")


def test_csrf_attack(get_pubip):
    """Test csrf attack."""
    pub_ip = get_pubip
    output = attackslib.code_injection_attack(pub_ip, secure=False)
    assert "support ID" in output
    print("======================  CSRF attack blocked successfully.  =============")


def test_cross_script_attack_mouse_over_param(get_pubip):
    """Test cross script attack with param."""
    pub_ip = get_pubip
    output = attackslib.cross_script_attack_mouse_over_param(pub_ip)
    assert "support ID" in output
    print("===================  Cross script attack blocked successfully.  ===========")


# send valid traffic
def test_buy_stocks(get_pubip):
    """Test buy stocks valid request."""
    pub_ip = get_pubip
    success = False
    for x in range(5):
        req = arcadialib.buy_stocks(pub_ip, "buy_stocks.json", secure=False)
        if '"status":"success"' in req:
            success = True
            break
    assert success
    print("======================  Buy stocks API validated successfully.  =============")


def test_transfer_money(get_pubip):
    """Test transfer money request."""
    pub_ip = get_pubip
    req = arcadialib.transfer_money(pub_ip, "transfer_money.json", secure=False)
    assert req.status_code == 200
    print("======================  Transfer money API validated successfully.  =============")


def test_sell_stocks(get_pubip):
    """Test sell stocks valid request."""
    pub_ip = get_pubip
    req = arcadialib.sell_stocks(pub_ip, "sell_stocks.json", secure=False)
    assert '"status":"success"' in req
    print("======================  Sell stocks API validated successfully.  =============")


def test_last_transactions(get_pubip):
    """Test last transactions valid request."""
    pub_ip = get_pubip
    req = arcadialib.last_transactions(pub_ip, secure=False)
    assert 'Last Transactions' in req
    print("======================  Last transactions API validated successfully.  =============")
