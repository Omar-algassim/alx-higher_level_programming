#!/usr/bin/python3
"""rtakes in a URL and an email address, sends a POST request to
the passed URL with the email
as a parameter, and finally displays the body of the response."""


import requests
import sys

if "__main__" == __name__:
    url = sys.argv[1]
    email = sys.argv[2]
    data = {"email": email}
    requests.post(url=url, data=data)
    web = requests.get(url)
    web.headers.get('email')
