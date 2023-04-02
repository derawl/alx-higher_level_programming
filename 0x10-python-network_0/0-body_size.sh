#!/bin/bash
# echo a length of the requests body
echo $(curl -sI "$url" | grep -i "Content-length" | awk '{print $2}')
