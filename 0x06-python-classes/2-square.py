#!/usr/bin/python3
"""This module defines the Square class."""


class Square:
    """Represents a square."""


def __init__(self, size=0):
    """ size must be an integer, otherwise raise a TypeError
    size is less than 0, raise a ValueError
    Size setter to take in Data for size square """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    else:
        self.__size = size
