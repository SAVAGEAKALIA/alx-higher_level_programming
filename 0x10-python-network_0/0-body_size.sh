#!/bin/bash
# Call Curl command and pass to grep to print number of lines
curl -sI "$1" | grep -i "Content-Length" | awk '{print $2}' | tr -d '\r'
