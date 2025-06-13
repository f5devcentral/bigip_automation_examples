#!/bin/bash
export emailid=student@f5lab.dev
export PATH="~/f5lab/scripts:$PATH"
chmod +x ~/f5lab/scripts/*

# Copy additional lab shortcuts to jump host desktop
cp ~/f5lab/scripts/desktop-files/* /mnt/c/Users/user/Desktop/

# Create alias to determine jump host's public IP address
alias myip='curl https://ifconfig.me/ip;echo'

# Create aliases for common Terraform commands
alias tf='terraform'
alias tfi='terraform init'
alias tfp='terraform plan'
alias tfo='terraform output'
alias tfa='terraform apply -auto-approve'
alias tfd='terraform destroy -auto-approve'

# Create aliases for easy lab BIG-IP access
alias bigip1='ssh -i ./f5lab.key admin@$(terraform output --raw bigip1_mgmt_public_ip)'
alias bigip2='ssh -i ./f5lab.key admin@$(terraform output --raw bigip2_mgmt_public_ip)'
