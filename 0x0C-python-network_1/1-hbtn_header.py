#!/usr/bin/python3
""" documentation """
from urllib.request import urlopen, Request
from sys import argv


if __name__ == "__main__":
    with urlopen(Request(argv[1])) as response:
        headers = response.info()
        print(headers['X-Request-Id'])
