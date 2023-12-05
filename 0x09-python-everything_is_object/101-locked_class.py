#!/usr/bin/python3
""" A locked Class documentation """


class LockedClass:
    """
    A class with restricted attr creation, allowing only 'first_name'.

    Attributes:
    - __slots__: A list specifying the allowed attribute names.

    Methods:
    (self, first_name): Constructor to init the 'first_name' attr.
    """

    __slots__ = ['first_name']

    def __init__(self, first_name=''):
        """
        Initializes an instance of LockedClass.

        Parameters:
        - first_name (str): The value to set for the 'first_name' attribute.
        """
        self.first_name = first_name
