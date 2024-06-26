#!/bin/bash
# This  Bash script that takes in a URL, sends a request to that URL, and displays the size of the body of the response

# Check if URL argument is provided
if [ -z "$1" ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi
curl -sI "$1" | grep -i Content-Length | awk '{print $2}'