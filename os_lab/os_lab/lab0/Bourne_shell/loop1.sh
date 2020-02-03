#!/bin/sh
for filename in *.sh
do 
	echo "Variable filename is set to $filename"
	ls -l $filename
	wc -l $filename
done
