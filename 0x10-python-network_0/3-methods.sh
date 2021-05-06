#!/bin/bash
# All ALLOWED HTTP
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-
