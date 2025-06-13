# Shortcut to browse to both BIG-IPs

export BROWSER=wslview
echo "Accept the SSL warnings and login as 'admin' with password: $(terraform output --raw random_password)"
wslview https://$(terraform output --raw bigip1_mgmt_public_ip)
wslview https://$(terraform output --raw bigip2_mgmt_public_ip)

