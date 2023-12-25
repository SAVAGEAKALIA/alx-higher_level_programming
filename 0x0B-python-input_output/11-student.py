#!/usr/bin/python3
""" File for the  Input/Output Project"""


class Student:
    """Class that defines a student."""

    def __init__(self, first_name, last_name, age):
        """
        Initialize a Student instance with first_name, last_name, and age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieve a dictionary representation of a Student instance.

        Args:
            attrs (list):attribute names to include in the result.

        Returns:
            dict: Dictionary representation of the Student instance.
        """
        result = {}

        # If attrs is not provided, include all attributes
        if attrs is None:
            attrs = \
                [a_name for a_name in dir(self) if not a_name.startswith('__')]

        # Iterate over the specified attributes
        for attribute_name in attrs:
            # Filter out private attributes
            if not attribute_name.startswith('__'):
                try:
                    att_value = getattr(self, attribute_name)
                    # Check if the attribute is of a serializable type
                    if isinstance(att_value, (list, dict, str, int, bool)):
                        result[attribute_name] = att_value

                except AttributeError:
                    # case where the attribute doesn't exist
                    pass

        return result

    def reload_from_json(self, json):
        """
        Replace all attributes of the Student instance using a dictionary.

        Args:
            json (dict): Dictionary representing the attributes to be replaced.
        """
        for key, value in json.items():
            setattr(self, key, value)
