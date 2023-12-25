#!/usr/bin/python3
"""File for the Input/Output Project"""
import json


def to_json_string(my_obj):
    """
    Returns the JSON representation of an object as a string.

    Args: my_obj: The object to convert to JSON.

    Returns: The JSON string representation of the object.
    """
    return json.dumps(my_obj)
