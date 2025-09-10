#!/bin/bash
rm *tfstate*
rm example*
rm *rendered*
rm *.pem
rm *.svg

if [ $? -eq 0 ]
then
  echo "The script ran ok"
else
  echo "The script failed" >&2
fi

