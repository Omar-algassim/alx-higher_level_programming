#!/usr/bin/python3
""" post header"""


import urllib.request
import urllib.parse
import sys

url = sys.argv[1]
email = sys.argv[2]
data_dict = {"email": email}
data = urllib.parse.urlencode(data_dict)
data = data.encode('utf8')
with urllib.request.urlopen(url, data) as response:
    print(response.read().decode('utf8'))
