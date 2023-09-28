#!/bin/bash
# a Bash script that takes in a URL, sends a request to that URL, and displays the size of the body of the response

if [[ $# -lt 1 ]]; then
    exit 1
fi
url="$1"
curl -sI "$url" | grep "Content-Length" | cut -d ' ' -f 2