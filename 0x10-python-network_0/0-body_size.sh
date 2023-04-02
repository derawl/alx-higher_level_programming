#!/usr/bin/bash
#echos the length of the response body

url=$1

size=$(curl -sI "url" | grep -i "Content-length" | awk '{print $2}')

echo $size