#!/bin/bash

yes | cp -rf /root/.ssh/id_rsa.pub /shared_data/git_public_key
yes | cp -rf /root/.ssh/id_rsa /shared_data/git_private_key

chown -R 1000:1000 /shared_data/git_private_key

# Start the SSH service
/usr/sbin/sshd -D
