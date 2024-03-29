#!/usr/bin/python3
""" retrive the info of request"""


import requests
import sys


url = sys.argv[1]
if "__main__" == __name__:
    with requests.get(url) as web:
        print(web.headers.get('X-Request-Id'))
