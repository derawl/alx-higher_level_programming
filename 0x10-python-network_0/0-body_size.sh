#!/bin/bash
url=$1
echo $(curl -sI "$url" | grep -i "Content-length" | awk '{print $2}')
