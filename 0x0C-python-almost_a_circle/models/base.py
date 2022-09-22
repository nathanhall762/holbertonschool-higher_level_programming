#!/usr/bin/python3
""" documentation """
import json


class Base:
    """ documentation """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """ returns the JSON string representation of input """
        if list_dictionaries is None:
            return []
        return json.dumps(list_dictionaries)
