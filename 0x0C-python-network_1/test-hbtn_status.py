#!/usr/bin/python3
"""documentation"""
import urllib.request

if __name__ == "__main__":
    request = urllib.request.Request('https://tulsaanimalrehab.com')

    with urllib.request.urlopen(request) as response:
        print(type(response))
        stuff = response.read()
        print(type(stuff))
        utf8_stuff = stuff.decode('utf-8')
        print(type(utf8_stuff))

        print('Body response:')
        print('\t- type: {_type}'.format(_type=type(stuff)))
        print('\t- content: {_stuff}'.format(_stuff=stuff))
        print('\t- utf8 content: {_utf8_c}'.format(_utf8_c=utf8_stuff))
