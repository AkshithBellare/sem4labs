#!/bin/sh
for text_file in max.txt min.txt
do
	echo "editing the file $text_file"
	sed -e $text_file > temp
	mv -f temp $text_file
done
