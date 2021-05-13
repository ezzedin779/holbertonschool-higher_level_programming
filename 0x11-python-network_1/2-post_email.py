#!/usr/bin/python3
""" POST REQUEST WITH EMAIL """
import sys
import urllib.request
import urllib.parse


if __name__ == "__main__":
    link = sys.argv[1]
    val = {"email": sys.argv[2]}
    d = urllib.parse.urlencode(val).encode("ascii")
    req = urllib.request.Request(link, d)
    with urllib.request.urlopen(req) as response:
        print(response.read().decode("utf-8"))
