#!/usr/bin/python3
""" documentation """


def write_file(filename="", text=""):
    """ documentation """
    with open(filename, mode="w", encoding="utf-8") as f:
        return f.write(text)
