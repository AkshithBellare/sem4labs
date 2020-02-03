#!/bin/sh
name="fantastic"
echo "name is $name"
name=`echo $name | tr 'a' 'i'`
echo "name has changed to $name"

