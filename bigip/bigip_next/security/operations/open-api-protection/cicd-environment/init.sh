mkdir jenkinshome
mkdir shared

cp ~/.ssh/id_rsa ./shared/app_host_private_key

sudo chown -R 1000:1000 ./jenkinshome
sudo chown -R 1000:1000 ./shared


