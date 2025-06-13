#!/bin/bash
DESTINATION="/mnt/c/Users/user/Desktop"
terraform graph | dot -Tsvg > terraform_dependancy_graph.svg
cp ./terraform_dependancy_graph.svg $DESTINATION

if [ $? -eq 0 ]
then
  echo "The script ran ok"
else
  echo "The script failed" >&2
fi

