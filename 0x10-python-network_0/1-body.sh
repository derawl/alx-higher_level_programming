#!/bin/bash
# This script takes in a URL, sends a GET request to the URL, and displays the body of the response

curl -sL "$1" -X GET -D ./header -o ./output; if awk 'NR==1 && $2==200 {exit 0} {exit 1}' ./header; then cat ./output; fi