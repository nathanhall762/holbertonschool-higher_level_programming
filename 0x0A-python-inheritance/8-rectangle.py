#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry
""" documentation """


class Rectangle(BaseGeometry):
    """ documentation """
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        Rectangle.__width = width
        Rectangle.__height = height
