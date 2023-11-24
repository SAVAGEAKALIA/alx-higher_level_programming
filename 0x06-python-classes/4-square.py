#!/usr/bin/python3
"""This module defines the Square class."""

class Square:
    """Represents a square."""

    def __init__(self, size=0):
        """ size must be an integer, otherwise raise a TypeError
        
        size is less than 0, raise a ValueError
        Size setter to take in Data for size square """

        self.size = size
    
    @property
    def size(self):
        """ property Getter class to return setter """
        return self.__size
    
    @size.setter
    def size(self, value):
        """ Property setter for class Size """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
            """Calculate and return the area of the square"""
            return self.__size ** 2
