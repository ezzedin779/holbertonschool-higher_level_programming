#!/usr/bin/python3
""" Handling errors of requests """
import sys
import urllib.request
import urllib.error


if __name__ == "__main__":
    link = sys.argv[1]
    req = urllib.request.Request(link)
    try:
        with urllib.request.urlopen(req) as response:
            print(response.read().decode("ascii"))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
