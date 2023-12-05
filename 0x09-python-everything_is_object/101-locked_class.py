#!/usr/bin/python3
class LockedClass:
    """
    A class with restricted attribute creation, allowing only 'first_name'.

    Attributes:
    - __slots__: A list specifying the allowed attribute names.

    Methods:
    - __init__(self, first_name): Constructor to initialize the 'first_name' attribute.
    """

    __slots__ = ['first_name']

    def __init__(self, first_name=''):
        """
        Initializes an instance of LockedClass.

        Parameters:
        - first_name (str): The value to set for the 'first_name' attribute.
        """
        self.first_name = first_name
