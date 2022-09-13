#!/usr/bin/python3
""" documentation """


class Rectangle():
    """ documentation	"""
    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if isinstance(value, int):
            if value < 0:
                raise ValueError("height must be >= 0")
            self.__height = value
        else:
            raise TypeError("height must be an integer")

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if isinstance(value, int):
            if value < 0:
                raise ValueError("width must be >= 0")
            self.__width = value
        else:
            raise TypeError("width must be an integer")

    def area(self):
        return self.__height * self.__width

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (self.__height * 2) + (self.__width * 2)

    def __str__(self):
        string = ""
        if self.__height == 0 or self.__width == 0:
            return string
        for i in range(self.__height):
            if i == self.__height - 1:
                string += ('#' * self.__width)
            else:
                string += (('#' * self.__width) + '\n')
        return string

    def __repr__(self):
        w = str(eval('self.width'))
        h = str(eval('self.height'))
        return 'Rectangle(' + w + ', ' + h + ')'
