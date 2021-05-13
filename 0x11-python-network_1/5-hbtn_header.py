#!/usr/bin/python3
""" X-Request- Id """
import sys
import requests


if __name__ == "__main__":
    link = sys.argv[1]
    req = requests.get(link)
    print(req.headers.get("X-Request-Id"))
