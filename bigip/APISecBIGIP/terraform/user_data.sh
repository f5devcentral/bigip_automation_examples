#!/bin/bash
sudo rm -rf /var/lib/cloud/*
sudo apt upgrade -y
sudo apt update -y
sudo apt install docker.io -y
sudo docker pull registry.gitlab.com/arcadia-application/main-app/mainapp:latest
sudo docker pull registry.gitlab.com/arcadia-application/back-end/backend:latest
sudo docker pull registry.gitlab.com/arcadia-application/app2/app2:latest
sudo docker pull registry.gitlab.com/arcadia-application/app3/app3:latest
sudo docker pull registry.gitlab.com/arcadia-application/nginx/nginxoss:latest
