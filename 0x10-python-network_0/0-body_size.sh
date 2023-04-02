#!/bin/bash
# echo a length of the requests body
echo $(curl -sI "$1" | grep -i "Content-length" | awk '{print $2}')
