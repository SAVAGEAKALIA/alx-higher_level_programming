#!/bin/bash
if [ $# -ne 1 ]; then 
	echo "Arguments for server not complete"
	exit 1
fi

IP=$1

# Call Curl command and pass to grep to print number of lines

curl -sI "$IP" | grep -i "Content-Length" | awk '{print $2}' | tr -d '\r'
