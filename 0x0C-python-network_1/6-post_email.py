#!/usr/bin/python3
"""documentation"""
from sys import argv
import requests


if __name__ == "__main__":
    values = {'email': argv[2]}
    requests = requests.post(argv[1], data=values)

    print(requests.text)
