#!/usr/bin/python3
""" Some manip in GITHUB API """
import sys
import requests


if __name__ == "__main__":
    a = requests.auth.HTTPBasicAuth(sys.argv[1], sys.argv[2])
    req = requests.get("https://api.github.com/user", auth=a)
    print(req.json().get("id"))
