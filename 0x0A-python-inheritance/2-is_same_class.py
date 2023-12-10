#!/usr/bin/python3
""" Function to create Class """


def is_same_class(obj, a_class):
    """
    Returns True if the object is exactly an instance of the specified class;
    otherwise False.

    Args:
    - obj: An object to check.
    - a_class: The class to check against.

    Returns:
    - True if obj is an instance of a_class; False otherwise
    """
    if type(obj) is a_class:
        return True
    else:
        return False
