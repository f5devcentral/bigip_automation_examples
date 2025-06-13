touch example01a.f5lab.dev.cert
touch example01a.f5lab.dev.key
touch example01b.f5lab.dev.cert
touch example01b.f5lab.dev.key

if [ $? -eq 0 ]
then
  echo "The script ran ok"
else
  echo "The script failed" >&2
fi

