#!/bin/bash
# Send a GET request to the URL using curl with the custom header and display the response body
curl -sX GET -H "X-School-User-Id:98" "$1"
