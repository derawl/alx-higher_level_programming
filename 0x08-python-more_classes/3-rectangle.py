#!/usr/bin/python3
"""
This module is composed by a class that defines a Rectangle
"""


class Rectangle:
    """ Class that defines a rectangle """

    def __init__(self, width=0, height=0):
        """ Method that initializes the instance
        Args:
            width: width of the rectangle
            height: height of the rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ method that returns the value of the width
        Returns:
            width of the rectangle
        """

        return self.__width

    @width.setter
    def width(self, value):
        """ method that defines the width
        Args:
            value: width
        Raises:
            TypeError: if width is not an integer
            ValueError: if width is less than zero
        """

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ method that returns the value of the height
        Returns:
            height of the rectangle
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

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """method that returns the area of a rectangle

        Returns:
            rectangle area

        """
        return self.height * self.width

    def perimeter(self):
        """method that calculates the perimeter of a rectangle

        Returns:
            rectangle perimeter

        """
        if self.height == 0 or self.width == 0:
            return 0
        else:
            return (2 * self.height) + (2 * self.width)

    def __str__(self):
        """Methods that returns the shape of the rectangle in #

        Returns:
            str of the rectangle shape
        """
        rectangle_shape = ""
        if self.width == 0 or self.height == 0:
            return ''

        for i in range(self.height):
            rectangle_shape += ("#" * self.width) + "\n"

        return rectangle_shape
