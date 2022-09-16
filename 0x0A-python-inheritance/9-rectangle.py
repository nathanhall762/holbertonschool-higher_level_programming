#!/usr/bin/python3
""" documentation """


class BaseGeometry():
    """ documentation """
    def area(self):
        return (self.__width * self.__height)

    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """ documentation """
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        Rectangle.__width = width
        Rectangle.__height = height

    def area(self):
        return (self.__width * self.__height)

    def __str__(self):
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))