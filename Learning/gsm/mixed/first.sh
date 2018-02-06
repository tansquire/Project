#!/bin/sh
if [ "`ping -c 1 10.21.160.201`" ]
then
  echo 1
else
  echo 0
fi
