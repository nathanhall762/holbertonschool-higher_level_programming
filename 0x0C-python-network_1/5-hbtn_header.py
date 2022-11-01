#!/usr/bin/python3
"""documentation"""
from sys import argv
import requests


if __name__ == "__main__":
    request = requests.get(argv[1])
    print(request.headers.get('X-Request-Id'))
