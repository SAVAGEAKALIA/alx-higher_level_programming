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
            raise TypeError("{} must be an integer".format(self.name))
        if self.value <= 0:
            raise ValueError("{} must be greater than 0".format(self.name))
