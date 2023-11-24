#!/usr/bin/python3
"""This module defines the Square class."""


class Square:
    """Defines a square."""

    def __init__(self, size=0):
        """Initialize the square
        Set the size of the square.

        Args:
            value (int): The size value.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
