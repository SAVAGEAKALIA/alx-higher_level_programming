#!/usr/bin/python3
""" Function to check obj type """


def is_kind_of_class(obj, a_class):
    """
    Returns True if the object is a type class;
    otherwise False.

    Args:
    - obj: An object to check.
    - a_class: The class to check against.

    Returns:
    - True if obj is an instance of a_class; False otherwise
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
