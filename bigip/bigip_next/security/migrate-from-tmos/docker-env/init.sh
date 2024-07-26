pushd
cd ~/.ssh
ssh-keygen -y -f id_rsa > id_rsa.pub
cat id_rsa.pub >> authorized_keys
popd

mkdir keys
cp ~/.ssh/* ./keys