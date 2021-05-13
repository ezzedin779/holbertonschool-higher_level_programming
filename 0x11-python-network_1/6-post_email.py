#!/usr/bin/python3
""" POST REQUEST WITH EMAIL """
import sys
import urllib.request
import urllib.parse


if __name__ == "__main__":
    link = sys.argv[1]
    val = {"email": sys.argv[2]}
    req = requests.post(url, data=val)
    print(req.text)
