#!/usr/bin/python3
""" Create an empty class called Square
"""

class Square:
    """ Empty class with size private attribute
    """
    def __init__(self, size=0):
        """
                Instantiation with size
        Args:
            size: size of the square
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Returns the area of the square
        """
        return self.__size**2

    @property
    def size(self):
        """
        size getter. Returns size of a side
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        size setter. sets size of a side
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value