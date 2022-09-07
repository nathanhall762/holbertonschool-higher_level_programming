#!/usr/bin/python3
"""Square Class

This is a square

"""


class Square:
    """Summary of class here.

    Longer class information...
    Longer class information...

    Attributes:
        size: A boolean indicating if we like SPAM or not.
    """
    def __init__(self, size=0):
        """Inits SampleClass with blah."""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
