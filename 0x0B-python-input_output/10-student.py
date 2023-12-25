#!/usr/bin/python3
""" File for the  Input/Output Project"""


class Student:
    """A Public Class student created to show Json Use"""

    def __init__(self, first_name, last_name, age):
        """ Init instance creation """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Write a function that returns the
        dictionary description with simple data structure
        (list, dictionary, string, integer and boolean)
        for JSON serialization of an object
        args:
            obj
        """
        result = {}

        # If attrs is not provided, include all attributes
        if attrs is None:
            attrs = [attribute_name for attribute_name in dir(self) if not attribute_name.startswith('__')]
        # Iterate over the attributes of the object
        for attribute_name in attrs:
            # Filter out private attributes
            if not attribute_name.startswith('__'):
                try:
                    attribute_value = getattr(self, attribute_name)

                    # Check if the attribute is of a serializable type
                    if isinstance(attribute_value, (list, dict, str, int, bool)):
                        result[attribute_name] = attribute_value
                except AttributeError:
                    pass
        return result
