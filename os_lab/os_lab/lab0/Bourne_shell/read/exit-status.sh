#!/bin/sh
ls /nosuchdir
echo "status is $? from command:ls /nosuchdir"
ls /tmp
echo "status is $?"
