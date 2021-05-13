#!/usr/bin/python3
""" Fetching the intranet status """
import urllib.request


if __name__ == "__main__":
    req = urllib.request.Request("https://intranet.hbtn.io/status")
    with urllib.request.urlopen(req) as response:
        b = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(b)))
        print("\t- content: {}".format(b))
        print("\t- utf8 content: {}".format(b.decode("utf-8")))
