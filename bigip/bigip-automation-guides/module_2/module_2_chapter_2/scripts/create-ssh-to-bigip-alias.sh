#!/bin/bash

export bigip1_mgmt_public_ip=$(aws ec2 describe-instances --filters "Name=tag:Name,Values=bigip1-az1-3nic-payg" --query "Reservations[*].Instances[*].PublicIpAddress" --output text)
export bigip2_mgmt_public_ip=$(aws ec2 describe-instances --filters "Name=tag:Name,Values=bigip2-az2-3nic-payg" --query "Reservations[*].Instances[*].PublicIpAddress" --output text)
alias bigip1='ssh -i ./f5lab.key admin@${bigip1_mgmt_public_ip}'
alias bigip2='ssh -i ./f5lab.key admin@${bigip2_mgmt_public_ip}'
if [ $? -eq 0 ]
then
  echo "The script ran ok"
else
  echo "The script failed" >&2
fi

