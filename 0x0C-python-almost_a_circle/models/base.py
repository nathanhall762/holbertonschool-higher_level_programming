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

    @staticmethod
    def to_json_string(list_dictionaries):
        """ returns the JSON string representation of list_dictionaries """

        if len(list_dictionaries) < 1:
            return []
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ writes the JSON string representation of list_objs to a file """

        filename = cls.__name__ + '.json'
        with open(filename, mode='w') as f:
            if len(list_objs) < 1:
                return f.write(cls.to_json_string(None))
            json_add = []
            for element in list_objs:
                json_add.append(element.to_dictionary())
            return f.write(cls.to_json_string(json_add))
