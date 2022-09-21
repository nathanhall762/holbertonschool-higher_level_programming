#!/usr/bin/python3
""" documentation """
from models.base import Base
from models.rectangle import Rectangle


class Square(Rectangle):
    """ documentation """

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(width=size, height=size, x=x, y=y, id=id)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        return "[{}] ({}) {}/{} - {}".format(self.__class__.__name__,
                                             self.id, self.x, self.y,
                                             self.width)

    def update(self, *args, **kwargs):
        """ updates square attributes """

        if len(kwargs) > 0:
            for k, v in kwargs.items():
                setattr(self, k, v)
        else:
            for idx in range(len(args)):
                if idx == 0:
                    self.id = args[idx]
                if idx == 1:
                    self.size = args[idx]
                if idx == 2:
                    self.x = args[idx]
                if idx == 3:
                    self.y = args[idx]
