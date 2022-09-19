#!/usr/bin/python3
""" documentation """


def read_file(filename=""):
    with open(filename, encoding="utf-8") as myFile:
        print(myFile.read())
