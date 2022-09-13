#!/usr/bin/python3
""" documentation """


class Rectangle:
    """ documentation	"""
    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if isinstance(value, int):
            if value < 0:
                raise ValueError("height must be >= 0")
            self._height = value
        else:
            raise TypeError("height must be an integer")

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if isinstance(value, int):
            if value < 0:
                raise ValueError("width must be >= 0")
            self._width = value
        else:
            raise TypeError("width must be an integer")
