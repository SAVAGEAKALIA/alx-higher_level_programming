#!/usr/bin/python3
""" A Class for BaseGeometry """


class BaseGeometry:
    """ Base Geometry Class """

    def __init__(self):
        self.value = None
        self.name = None

    def area(self):
        """ Raises exception error"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ Integer Validator for Base Geometry Class """
        self.value = value
        self.name = name

        if not isinstance(self.value, int):
            raise TypeError("<name> must be an integer")
        if self.value <= 0:
            raise ValueError("<name> must be greater than 0")


class Rectangle(BaseGeometry):
    """ Subclass of BaseGeometry """

    def __init__(self, width, height):
        """ Instance of  class for width and height """
        super().__init__()
        self.integer_validator("width", width)  # Validate width
        self.integer_validator("height", height)  # Validate height

        self.__width = width
        self.__height = height

    def area(self):
        """ Calculates the Area """
        return self.__width * self.__height

    def __str__(self):
        """ Return the String value of Class """
        return f"[Rectangle] {self.__width}/{self.__height}"
