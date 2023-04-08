#!/bin/bash
# Send a GET request to the URL using curl with the custom header and display the response body
curl -s -X GET -H "X-School-User-Id: 98" -D ./header -o ./output "$1" && status_code=$(awk 'BEGIN {code=0} $1=="HTTP/1.1" || $1=="HTTP/2" {code=$2} END {print code}' ./header) && if [ $status_code -eq 200 ]; then cat ./output; elif [ $status_code -eq 400 ]; then echo "Bad Request: The server cannot process the request due to invalid syntax or a missing header."; elif [ $status_code -eq 404 ]; then echo "Not Found: The requested route was not found on the server."; else echo "Error: Received an unexpected HTTP status code: $status_code"; fi

