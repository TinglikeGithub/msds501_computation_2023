file='ex03_input.sh'
x=`cat $file`

for line in $x
do
    echo `$line`
done