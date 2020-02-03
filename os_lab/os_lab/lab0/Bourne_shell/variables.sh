#!/bin/sh
# an example with variables
filename="/etc/passwd"
echo "check the permission on $filename"
ls -l $filename
echo "Find out how many accounts are there in the system"
wc -l $filename
