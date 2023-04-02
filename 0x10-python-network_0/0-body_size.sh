#!/bin/bash
size=$(curl -sI "$1" | grep -i "Content-length" | awk '{print $2}')
echo $size