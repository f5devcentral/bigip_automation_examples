#!/bin/bash
set -e
FILE=f5lab_aws_keypair.pem
if test -f "$FILE"; then
echo "$FILE exists, remove $FILE and try again!" && exit 1
fi
aws ec2 create-key-pair --key-name f5lab_aws_keypair --query 'KeyMaterial' --output text > $FILE
chmod 400 f5lab_aws_keypair.pem
if [ $? -eq 0 ]
then
  echo "The script ran ok"
else
  echo "The script failed" >&2
fi

