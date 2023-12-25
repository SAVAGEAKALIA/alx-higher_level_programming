#!/usr/bin/python3
""" File for the  Input/Output Project"""
import json


def save_to_json_file(my_obj, filename):
    """
    Function that writes an object to
    a text file using JSON string representation

    args: my_obj, filename
    """

    with open(filename, 'w', encoding='utf-8') as json_file:
        json.dump(my_obj, json_file)
