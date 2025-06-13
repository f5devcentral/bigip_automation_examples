#!/bin/bash

printf "\nAWS Credentials:\n"
printf "   AWS Console URL:      %s\n" ${TF_VAR_AWS_CONSOLE_LINK}
printf "   AWS Console Username: %s\n" ${TF_VAR_AWS_USER}
printf "   AWS Console Password: %s\n\n" ${TF_VAR_AWS_PASSWORD}

if [ $? -eq 0 ]
then
  echo "The script ran ok"
else
  echo "The script failed" >&2
fi

