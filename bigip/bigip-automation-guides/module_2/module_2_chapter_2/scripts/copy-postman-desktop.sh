#!/bin/bash

cp ~/f5lab/postman/* /mnt/c/Users/user/Desktop/

if [ $? -eq 0 ]
then
  echo "The script ran ok"
else
  echo "The script failed" >&2
fi
