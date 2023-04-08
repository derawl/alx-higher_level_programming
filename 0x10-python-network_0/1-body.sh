#!/bin/bash
# This script takes in a URL, sends a GET request to the URL, and displays the body of the response
curl -sL "$1" -X GET -D ./header -o ./output && awk 'BEGIN {code=0} $1=="HTTP/1.1" || $1=="HTTP/2" {code=$2} END {if (code==200) exit 0; else exit 1}' ./header && cat ./output
