#!/usr/bin/python3
"""documentation"""
import requests

if __name__ == "__main__":
    request = requests.get('https://intranet.hbtn.io/status')

    print('Body response:')
    print('\t- type: {_type}'.format(_type=type(request.text)))
    print('\t- content: {_stuff}'.format(_stuff=request.text))
