#!/usr/bin/python3
""" Write a function that prints a square with the character #
"""


def print_square(size):
    """ Function that prints Square

    args: size is the argument passed

    Returns square
    """
    if not isinstance(size, int):
        raise ValueError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")

    for x in range(size):
        for i in range(size):
            print("#", end="")
            i += 1
        print()
