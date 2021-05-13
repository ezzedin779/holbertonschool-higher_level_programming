#!/usr/bin/python3
""" SEND POST REQ WITH A LETTER """
import requests
import sys


if __name__ == "__main__":
    if (argv) == 2:
        q = argv[1]
    else:
        q = ""
    req = requests.post('http://0.0.0.0:5000/search_user', data={'q': q})
    try:
        res = req.json()
        if res == {}:
            print("No result")
        else:
            print("[{}] {}".format(res.get("id"), res.get("name")))
    except:
        print("Not a valid JSON")
