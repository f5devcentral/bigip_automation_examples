"""Arcadia app library functions."""

import requests
import os
import re

headers = {'Content-type': 'application/json'}
current_folder_path = os.path.dirname(__file__)
parent_folder_path = os.path.dirname(current_folder_path)
data_folder_path = os.path.join(parent_folder_path, "data/")


def check_arcadia(pub_ip, secure=False):
    """Check if application is running successfully."""
    
    if secure:
        #req = requests.request('GET','https://' + str(pub_ip), verify=False)
        req = requests.get('https://' + str(pub_ip), verify=False)
    else:
        #req = requests.request('GET','http://' + str(pub_ip))
        req = requests.get('http://' + str(pub_ip))
    print(req)
    if req.status_code != 200:
        return "not able to access arcadia server!"
    txt = req.text
    s = re.search("Welcome to Arcadia Finance website", txt)
    if s:
        return 'Arcadia application running successfully.'
    else:
        return "arcadia application inaccessible!"


def check_snap(dns, secure=False):
    """Check if snap page is accessible."""
    if secure:
        req = requests.get('https://' + str(dns), verify=False)
    else:
        req = requests.get('http://' + str(dns))
    if req.status_code != 200:
        return "not able to access snap server!"
    txt = req.text
    s = re.search("Welcome to serverless NGINX App Protect", txt)
    if s:
        return 'snap default page running successfully.'
    else:
        return "snap default page inaccessible."


def buy_stocks(pub_ip, json_file, secure=False):
    """Buy stock request."""
    json_file_path = data_folder_path + json_file
    if secure:
        req = requests.post('https://' + str(pub_ip) + "/trading/rest/buy_stocks.php",
                            data=open(json_file_path, 'rb'), headers=headers, verify=False)
    else:
        req = requests.post('http://' + str(pub_ip) + "/trading/rest/buy_stocks.php",
                            data=open(json_file_path, 'rb'), headers=headers)
    if req.status_code != 200:
        return "Unable to buy stocks in arcadia server!"
    return req.text


def sell_stocks(pub_ip, json_file, secure=False):
    """Sell stock request."""
    json_file_path = data_folder_path + json_file
    if secure:
        req = requests.post('https://' + str(pub_ip) + "/trading/rest/sell_stocks.php", data=open(json_file_path, 'rb'),
                            headers=headers, verify=False)
    else:
        req = requests.post('http://' + str(pub_ip) + "/trading/rest/sell_stocks.php", data=open(json_file_path, 'rb'),
                            headers=headers)
    if req.status_code != 200:
        return "Unable to sell stocks in arcadia server!"
    return req.text


def transfer_money(pub_ip, json_file, secure=False):
    """Transfer money request."""
    json_file_path = data_folder_path + json_file
    if secure:
        req = requests.post('https://' + str(pub_ip) + "/trading/rest/execute_money_transfer.php",
                            data=open(json_file_path, 'rb'), headers=headers, verify=False)
    else:
        req = requests.post('http://' + str(pub_ip) + "/trading/rest/execute_money_transfer.php",
                            data=open(json_file_path, 'rb'), headers=headers)
    return req


def last_transactions(pub_ip, secure=False):
    """Get last transactions details."""
    if secure:
        req = requests.get('https://' + str(pub_ip) + "/trading/transactions.php", verify=False)
    else:
        req = requests.post('http://' + str(pub_ip) + "/trading/transactions.php")
    if req.status_code != 200:
        return "not able to access arcadia server!"
    return req.text
