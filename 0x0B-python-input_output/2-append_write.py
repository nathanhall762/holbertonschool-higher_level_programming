#!/usr/bin/python3
""" documentation """


def append_write(filename="", text=""):
    """ documentation """
    with open(filename, mode="a") as f:
        return f.write(text)
