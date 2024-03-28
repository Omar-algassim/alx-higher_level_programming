#!/usr/bin/python3
""" post header"""


from urllib import request, parse
import sys
if __name__ == '__main__':
    url = sys.argv[1]
    email = sys.argv[2]
    data_dict = {"email": email}
    data = parse.urlencode(data_dict)
    data = data.encode('utf8')
    with request.urlopen(url, data) as response:
        print(response.read().decode('utf8'))
