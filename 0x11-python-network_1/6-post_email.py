#!/usr/bin/python3
""" POST REQUEST WITH EMAIL """
import sys
import requests


if __name__ == "__main__":
    link = sys.argv[1]
    val = {"email": sys.argv[2]}
    req = requests.post(link, data=val)
    print(req.text)
