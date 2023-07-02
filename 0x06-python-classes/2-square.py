#!/usr/bin/python3
"""Square module. With a size to it this time"""


class Square:
    """The square class"""
    def __init__(self, size=0):
        """Initialize the objects attributes"""
        self.__size = size

    @size.setter
    def size(self, val):
        try:
            if val.isdigit():
                self.__size = val
        except(ValueError):
            print("size must be an integer")
