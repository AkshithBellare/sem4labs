#!/bin/sh
for filename in "$@"
do 
	echo "examining $filename"
	wc -l $filename
done
