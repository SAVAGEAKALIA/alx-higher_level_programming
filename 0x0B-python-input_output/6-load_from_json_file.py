#!/usr/bin/python3
""" File for the  Input/Output Project"""
import json


def load_from_json_file(filename):
    """
    Function that creates an object from
    a text file using JSON string representation

    args: filename
    Returns:
        obj: The Python object loaded from the JSON file.
    """

    with open(filename, mode='r', encoding='utf-8') as json_file:
        loaded_obj = json.load(json_file)

    return loaded_obj

if __name__ == "__main__":
    load_from_json_file(filename)
