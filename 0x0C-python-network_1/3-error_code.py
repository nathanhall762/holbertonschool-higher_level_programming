#!/usr/bin/python3
"""documentation"""
from sys import argv
from urllib.error import HTTPError
from urllib.parse import urlencode
from urllib.request import Request, urlopen

if __name__ == "__main__":
    url = argv[1]

    request = Request(url)

    try:
        with urlopen(request) as response:
            print(response.read().decode("utf-8"))
    except HTTPError as ex:
        print('Error Code: {}',.format(ex.code))
