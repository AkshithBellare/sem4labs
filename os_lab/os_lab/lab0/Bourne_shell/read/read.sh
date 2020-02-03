#!/bin/sh
echo "would you like to exit" 
read var_name
if ["$var_name" = yes]
then
	echo "exiting"
	exit 0
fi
