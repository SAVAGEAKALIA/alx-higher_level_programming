#!/usr/bin/python3
""" File for the  Input/Output Project"""


def class_to_json(obj):
    """
    Write a function that returns the
    dictionary description with simple data structure
    (list, dictionary, string, integer and boolean)
    for JSON serialization of an object
    args:
        obj
    """
    result = {}

    # Iterate over the attributes of the object
    for attribute_name in dir(obj):
        # Filter out private attributes
        if not attribute_name.startswith('__'):
            attribute_value = getattr(obj, attribute_name)

            # Check if the attribute is of a serializable type
            if isinstance(attribute_value, (list, dict, str, int, bool)):
                result[attribute_name] = attribute_value

    return result
