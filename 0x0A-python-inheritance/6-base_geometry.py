#!/usr/bin/python3
""" A Class to raise Exception Error """


class BaseGeometry:
    """ Prints exception error message """

    def area(self):
        """ Raises exception error"""
        raise Exception("area() is not implemented")
