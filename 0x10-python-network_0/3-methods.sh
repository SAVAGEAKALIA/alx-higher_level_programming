#!/bin/bash
# Bash script that takes in a URL and displays all HTTP methods the server will accept
curl -sI -X OPTIONS "$URL" | grep "Allow:" | cut -d ' ' -f2-
