#!/usr/bin/python3
""" request an alx url """


import urllib.request

if __name__ == "__main__":
    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as respons:
        print('body respons:')
        print(f"\t- type: {type(respons.read())}")
        print(f"\t- content: {respons.read()}")
        print(f"\t- utf8 content: {respons.read()}")
        