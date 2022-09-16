#!/usr/bin/python3
""" documentation """
BaseGeometry = __import__('9-rectangle').BaseGeometry
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ documentation """
    def __init__(self, size):
        self.integer_validator("size", size)
        Rectangle(size, size)
