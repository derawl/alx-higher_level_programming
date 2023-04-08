#!/bin/bash
# Script that returns the allowed http methods for a url
curl -sI -X OPTIONS "$1" | grep -i "^allow:" | cut -d' ' -f2-
