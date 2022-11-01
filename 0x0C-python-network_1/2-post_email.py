#!/usr/bin/python3
"""documentation"""
from sys import argv
from urllib import request
from urllib.parse import urlencode
from urllib.request import Request, urlopen

if __name__ == "__main__":
    values = {'email': argv[2]}
    url = argv[1]
    data = urlencode(values)
    data = data.encode('ascii')

    request = Request(url, data)

    with urlopen(request) as response:
        print(response.read().decode("utf-8"))
