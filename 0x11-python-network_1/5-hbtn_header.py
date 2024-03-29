#!/usr/bin/python3
"""retrive the id of the request"""


import requests
import sys

url = sys.argv[1]
if "__main__" == __name__:
    web = requests.get(url)
    print(web.headers.get('X-Request-Id'))
