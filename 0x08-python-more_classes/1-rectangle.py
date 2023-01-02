#!/usr/bin/python3

"""
1-rectangle: Defines a class of a rectangle
"""


class Rectangle:
    """Creates a rectangle class
    """

    def __init__(self, height="0", width="0"):
        self.__height = height
        self.__width = width

    @property
    def width(self):
        """Methods set the value of width
        :returns value of the width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Methods set the value of width
        Args:
            value: integer value of width
        :return Nothing
        :raise TypeError if value is not an integer
        :raise ValueError if value is less than zero
        """
        if type(value) is not int:
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        else:
            self.__width = value

    @property
    def height(self):
        """Methods set the value of width
        :returns value of the width
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Methods set the value of height
        Args:
            value: integer value of height
        :return Nothing
        :raise Type error if value is not an integer
        :raise Value error if value is less than zero
        """
        if type(value) is not int:
            raise TypeError('height must be an integer')
        elif value < 0:
            raise ValueError('height must be >= 0')
        else:
            self.__height = value
