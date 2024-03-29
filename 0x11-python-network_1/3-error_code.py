#!/usr/bin/python3
""" handel 404 error """


from urllib import request, error
import sys

url = sys.argv[1]

try:
    response = request.urlopen(url)
    print(response)
except error.HTTPError as e:
    print(f"Error code: {e.code}")
