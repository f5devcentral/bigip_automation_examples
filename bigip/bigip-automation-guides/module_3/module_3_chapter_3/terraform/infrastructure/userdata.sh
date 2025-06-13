#!/bin/bash

function checkStatus() {
  count=1
  sleep 10;
  STATUS=`cat /var/prompt/ps1`;
  while [[ ${STATUS}x != 'Active'x ]]; do
    echo -n '.';
    sleep 5;
    count=$(($count+1));
    STATUS=`cat /var/prompt/ps1`;

    if [[ $count -eq 60 ]]; then
      checkretstatus=\"restart\";
      return;
    fi
  done;
  checkretstatus=\"run\";
}

checkStatus

tmsh modify auth user admin password l8ibVeW45O0EXwMF
tmsh modify auth user admin { password admin }
tmsh modify auth user admin shell bash
tmsh save /sys config

tmsh modify sys global-settings gui-setup disabled
tmsh modify /sys http auth-pam-validate-ip off