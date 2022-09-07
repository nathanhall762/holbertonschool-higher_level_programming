#!/usr/bin/python3
"""Square Class

This is a square

"""


class Square:
    """Summary of class here.    """
    def __init__(self, size=0):
        """Inits SampleClass with blah."""
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """does a thing"""
        return self.__size ** 2

    def my_print(self):
        if self.__size == 0:
            print()
            return None
        for i in range(1, self.area() + 1):
            print('#', end='')
            if i % self.__size == 0 and i > 0:
                print()
