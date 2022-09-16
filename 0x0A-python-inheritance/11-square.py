#!/usr/bin/python3
""" documentation """
BaseGeometry = __import__('9-rectangle').BaseGeometry
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ documentation """
    def __init__(self, size):
        self.integer_validator("size", size)
        self.size = size
        Rectangle(size, size)

    def __str__(self):
        return ("[Square] {}/{}".format(self.size, self.size))
