#!/usr/bin/python3
"""
    contains class Square implements class Rectangle
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
        Square implements rectangle
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
            initialises Square (overrides Rectangle init)
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """
        Returns:
            the size of the square
        """
        return self.width

    @size.setter
    def size(self, value):
        """
            Sets the value of size
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")

        #sets the value to the same
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        Assigns key/value argument to attributes
        sets kwargs if args is empty
        sets args if is not empty
        Args:
            *args -  variable number of non keyword args
            **kwargs - variable number of keyword args
        """
        if len(args) == 0:
            for key, val in kwargs.items():
                self.__setattr__(key, val)
            return

        try:
            self.id = args[0]
            self.size = args[1]
            self.x = args[2]
            self.y = args[3]
        except IndexError:
            pass

    def __str__(self):
        """
            str function representation
        """
        return "[{}] ({}) {}/{} - {}".format(type(self).__name__,
                                             self.id, self.x, self.y,
                                             self.width)

    def update(self, *args, **kwargs):
        """
            Assigns key/value argument to attributes
            sets kwargs if args is empty
            kwargs is skipped if args is not empty
            Args:
                *args -  variable number of non keyword args
                **kwargs - variable number of keyword args
        """
        if len(args) == 0:
            for key, val in kwargs.items():
                self.__setattr__(key, val)
            return

        try:
            self.id = args[0]
            self.width = args[1]
            self.height = args[2]
            self.x = args[3]
            self.y = args[4]
        except IndexError:
            pass

    def to_dictionary(self):
        """
            Returns the dictionary representation of a Square
        """
        return {'id': getattr(self, "id"),
                'size': getattr(self, "width"),
                'x': getattr(self, "x"),
                'y': getattr(self, "y")}
