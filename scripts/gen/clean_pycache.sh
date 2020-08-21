#!/usr/bin/env bash
#echo "*** Running clean_pycs.sh ***"
if [ $# -eq 0 ]
  then
    echo "No arguments supplied. Assume path = ~/k3"
    find ~/k3 -name __pycache__ -delete
else
  find $1 -name __pycache__ -delete
fi
