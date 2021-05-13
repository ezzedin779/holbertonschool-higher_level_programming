#!/usr/bin/python3
""" Search in the STAR WARS API """
import sys
import requests


if __name__ == "__main__":
    req = requests.get("https://swapi.co/api/people", params={'search': sys.argv[1]})
    p = req.json()
    print("Number of results: {}".format(p.get('count')))
	for count in p.get('results'):
        print(count.get('name'))
