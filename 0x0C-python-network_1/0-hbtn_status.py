#!/usr/bin/python3
"""documentation"""
import urllib.request

if __name__ == "__main__":
    request = urllib.request.Request('https://intranet.hbtn.io/status')

    with urllib.request.urlopen(request) as response:
        stuff = response.read()
        utf8_stuff = stuff.decode('utf-8')

        print('Body response:')
        print('\t- type: {_type}'.format(_type=type(stuff)))
        print('\t- stuff: {_stuff}'.format(_stuff=stuff))
        print('\t- utf8 content: {_utf8_c}'.format(_utf8_c=utf8_stuff))
