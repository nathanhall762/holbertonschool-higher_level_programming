#!/usr/bin/python3
""" documentation """


def inherits_from(obj, a_class):
    """ documentation """
    if type(obj) is a_class or not isinstance(obj, a_class):
        return False
    else:
        return True
