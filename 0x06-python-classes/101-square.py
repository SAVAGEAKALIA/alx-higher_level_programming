#!/usr/bin/python3
"""This module defines the Square class."""

class Square:
    """Represents a square."""

    def __init__(self, size=0, position=(0, 0)):
        """ size must be an integer, otherwise raise a TypeError
        prints position and size
        size is less than 0, raise a ValueError
        Size setter to take in Data for size square """      

        self.size = size
        self.position = position

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

    @property
    def position(self):
        """ Retrieves Position of Square """
        return self.__position
    @position.setter
    def position(self, value):
        """ Setter for position attribute """
        if not isinstance(value, tuple) or len(value) != 2:
            if any (val <= 0 for val in value):
                raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
            """Calculate and return the area of the square"""
            return self.__size ** 2

    def my_print(self):
        """ Print in stdout the square with the character # """
        result = ""
        if self.size > 0:
            for _ in range(self.position[1]):
                result += "\n"
            for _ in range(self.size):
                result += " " * self.position[0] + "#" * self.size + "\n"
        else:
            result += "\n"
        return result.rstrip()
    def __str__(self):
        """String representation of the square."""
        return self.my_print()
