#!/bin/bash

envsubst < ./aws-console.template > /mnt/c/Users/Administrator/Desktop/"Amazon Web Services Sign-In.url"

if [ $? -eq 0 ]
then
  echo "The script ran ok"
else
  echo "The script failed" >&2
fi

