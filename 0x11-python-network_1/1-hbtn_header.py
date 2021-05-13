#!/usr//bin/python3
""" X-Request- Id """
import sys
import urllib.request


if __name__ == "__main__":
    link = sys.argv[1]
    req = urllib.request.Request(link)
    with urllib.request.urlopen(req) as response:
        print(dict(response.headers).get("X-Request-Id"))
