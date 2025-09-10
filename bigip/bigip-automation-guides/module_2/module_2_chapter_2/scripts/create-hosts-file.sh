#!/bin/bash
cp /mnt/c/Windows/System32/Drivers/etc/hosts /mnt/c/Windows/System32/Drivers/etc/hosts.$(date '+%s').bak
cp /mnt/c/Windows/System32/Drivers/etc/hosts /mnt/c/Windows/System32/Drivers/etc/hosts.$(date '+%s').bak
echo $(terraform output bigip1_mgmt_public_ip)    bigip1.f5lab.dev >> /mnt/c/Windows/System32/Drivers/etc/hosts
echo $(terraform output bigip2_mgmt_public_ip)    bigip2.f5lab.dev >> /mnt/c/Windows/System32/Drivers/etc/hosts


if [ $? -eq 0 ]
then
  echo "The script ran ok"
else
  echo "The script failed" >&2
fi

