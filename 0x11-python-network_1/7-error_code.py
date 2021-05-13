#!/usr/bin/python3
""" Handling errors of requests """
import sys
import requests


if __name__ == "__main__":
    link = sys.argv[1]
    req = requests.get(link)
    if req.status_code >= 400:
        print("Error code: {}".format(req.status_code))
    else:
        print(req.text)
