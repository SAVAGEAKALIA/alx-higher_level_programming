#!/usr/bin/python3
"""
Write a class Rectangle that defines a rectangle by: (based on 0-rectangle.py)
"""


class Rectangle:
    """ A class that forms a Rectangle

    args: width and height

    args must be argument if not raise value error
    """

    def __init__(self, width = 0, height = 0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """ Width property getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """ Width property setter """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """ height for class value Rectangle"""
        return self.height

    @height.setter
    def height(self, value):
        """ height property setter """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value
