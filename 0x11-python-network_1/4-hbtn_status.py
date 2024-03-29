#!/usr/bin/python3
""" get request """


import requests

if "__main__" == __name__:
    url = "https://alx-intranet.hbtn.io/status"
    response = requests.get(url)
    print("Body response:")
    print(f"\t- type: {type(response.content.decode('utf8'))}")
    print(f"\t- content: {response.content.decode('utf8')}")
