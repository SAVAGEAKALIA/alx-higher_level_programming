#!/usr/bin/python3
""" Say my name plus test """


def say_my_name(first_name, last_name=""):
    """ This is a function that prints name of the individual
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    name1 = first_name
    name2 = last_name

    print('My name is {} {}'.format(name1, name2))
