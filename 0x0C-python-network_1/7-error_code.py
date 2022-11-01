#!/usr/bin/python3
"""documentation"""
from sys import argv
import requests


if __name__ == "__main__":
    request = requests.get(argv[1])
    if request.status_code >= 400:
        print('Error code:', request.status_code)
    else:
        print(request.text)
