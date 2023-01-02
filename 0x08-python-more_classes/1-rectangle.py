#!/usr/bin/python3

"""
This module defines a class that defines a Rectangle
"""

class Rectangle:
    """Creates a rectangle class
    """

    def __init__(self, height=0, width=0):
        """ Method that initializes the instance
        Args:
            width: width of the rectangle
            height: height of the rectangle
        """
        self.__height = height
        self.__width = width

    @property
    def width(self):
        """Methods sets the value of width
        Returns:
            value of the width

        """
        return self.__width

    @width.setter
    def width(self, value):
        """Methods set the value of width
        Args:
            value: integer value of width
        Raises:
            TypeError: if value is not an integer
            ValueError: if widht is less than zero

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
        Returns:
            value of the height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """ method that defines the height
        Args:
            value: height
        Raises:
            TypeError: if height is not an integer
            ValueError: if height is less than zero
        """
        if type(value) is not int:
            raise TypeError('height must be an integer')
        elif value < 0:
            raise ValueError('height must be >= 0')
        else:
            self.__height = value
