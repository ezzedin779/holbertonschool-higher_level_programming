#!/bin/bash
# All ALLOWED HTTP
curl -sI 0.0.0.0:5000/route_4 | grep "Allow" | cut -d " " -f 2-
