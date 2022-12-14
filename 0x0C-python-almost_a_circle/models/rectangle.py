#!/usr/bin/python3
""" documentation """
import sys
from models.base import Base


class Rectangle(Base):
    """ documentation """
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """ returns the area of a triangle """

        return self.__width * self.__height

    def display(self):
        """ displays a rectangle """

        if self.__y != 0:
            for idx in range(0, self.__y):
                print()

        for i in range(0, self.__height):
            print((self.__x * ' ') + (self.__width * '#'))

    def __str__(self):
        return "[{}] ({}) {}/{} - {}/{}".format(self.__class__.__name__,
                                                self.id, self.__x, self.__y,
                                                self.__width, self.__height)

    def update(self, *args, **kwargs):
        """ updates rectangle attributes """

        if len(kwargs) > 0:
            for k, v in kwargs.items():
                setattr(self, k, v)
        else:
            for idx in range(len(args)):
                if idx == 0:
                    self.id = args[idx]
                if idx == 1:
                    self.width = args[idx]
                if idx == 2:
                    self.height = args[idx]
                if idx == 3:
                    self.x = args[idx]
                if idx == 4:
                    self.y = args[idx]

    def to_dictionary(self):
        """ documentation """
        return {
            'x': self.__x,
            'y': self.__y,
            'id': self.id,
            'height': self.__height,
            'width': self.__width,
        }
