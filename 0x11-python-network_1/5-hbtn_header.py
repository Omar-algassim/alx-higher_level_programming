#!/usr/bin/python3
"""retrive the id of the request"""


import requests
import sys

if "__main__" == __name__:
    url = sys.argv[1]
    web = requests.get(url)
    print(web.headers.get('X-Request-Id'))
