for i in lab1-*
do
 mv $i $i.zzz
 # do something on $i
done

for i in lab2-*
do
mv $i $(echo $i | sed -e "s/.zzz//")
 # do something on $i
done

if [ $? -eq 0 ]
then
  echo "The script ran ok"
else
  echo "The script failed" >&2
fi

