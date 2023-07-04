#!/usr/bin/python3
"""Square module. With a private instance of size, Type and Value gaurded"""


class Square:
    """The square class"""
    def __init__(self, size=0, position=(0, 0)):
        """Initialize the objects attributes"""
        self.size = size
        self.position = position

    @property
    def size(self):
        return self.__size

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, position):
        if not isinstance(position, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not isinstance(position[0], int) or not isinstance(position[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not len(position) == 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = position

    @size.setter
    def size(self, size):
        if not isinstance(size, int):
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
        if self.size == 0:
            print()
        else
            for i in range(self.position[1]):
                print()
            for j in range(self.size):
                print("{}{}".format(" " * self.position[0], '#'*self.size))
