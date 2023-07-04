#!/usr/bin/python3
"""Square module. With a private instance of size, Type and Value gaurded"""


class Square:
    """The square class"""
    def __init__(self, size=0):
        """Initialize the objects attributes"""
        self.__size = size
        @property
        def size(self):
            return self.size
        @size.setter
        def size(self, x):
            if not isinstance(size, int):
                raise TypeError("size must be an integer")
            elif size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size