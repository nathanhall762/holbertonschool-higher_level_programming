#!/usr/bin/python3
""" documentation """


class Rectangle:
    """ documentation	"""
    def __init__(self, width=0, height=0):
        self._height = height
        self._width = width

    @property
    def height(self):
        print("getter height")
        return self._height

    @height.setter
    def height(self, value):
        if value < 0:
            raise ValueError("height must be >= 0")
        if isinstance(value, int):
            self._height = value
        else:
            raise TypeError("height must be an integer")

    @property
    def width(self):
        print("getter width")
        return self._width

    @width.setter
    def width(self, value):
        if value < 0:
            raise ValueError("width must be >= 0")
        if isinstance(value, int):
            self._width = value
        else:
            raise TypeError("width must be an integer")
