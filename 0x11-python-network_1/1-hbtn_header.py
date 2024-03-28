#!/usr/bin/python3
"""takes in a URL, sends a request to the URL
and displays the valueof the X-Request-Id variable
found in the header of the response."""


import urllib.request
import sys

url = sys.argv[1]
with urllib.request.urlopen(url) as respons:
    print(respons.info()['X-Request-Id'])
