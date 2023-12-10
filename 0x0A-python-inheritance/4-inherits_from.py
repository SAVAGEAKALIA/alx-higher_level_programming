#!/usr/bin/python3
""" Function to check obj inheritance """


def inherits_from(obj, a_class):
    """
    Returns True if the object inheritance;
    otherwise False.

    Args:
    - obj: An object to check.
    - a_class: The class to check against.

    Returns:
    - True if obj is an instance of a_class; False otherwise
    """
    if isinstance(obj, a_class):
        # Check if obj type is not the same as the provided class
        if type(obj) is not a_class:
            return True
    return False
