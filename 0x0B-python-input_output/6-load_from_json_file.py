#!/usr/bin/python3
""" documentation """
import json


def load_from_json_file(filename):
    """ documentation """
    with open(filename, mode="r") as f:
        return json.loads(f)
