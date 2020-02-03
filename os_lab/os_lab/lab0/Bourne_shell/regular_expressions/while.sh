#!/bin/sh
i="1"
while [ $i -le 10 ]
do 
	echo "i is $i"
	i=`expr $i + 1`
done
