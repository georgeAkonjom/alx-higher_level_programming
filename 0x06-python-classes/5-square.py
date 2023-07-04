#!/usr/bin/python3
"""Square module. With a private instance of size, Type and Value gaurded"""


class Square:
    """The square class"""
    def __init__(self, size=0):
        """Initialize the objects attributes"""
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if isinstance(size, str):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """calcs and returns the area of a square object"""
        return pow(self.size, 2)

    def my_print(self):
        """prints the square using self.size as a metric"""
        i = 0
        for i in range(self.size):
            for i in range(self.size - 1):
                print("#", end="")
            print("#")
