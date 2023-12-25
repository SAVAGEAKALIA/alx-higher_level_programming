#!/usr/bin/python3
""" File for the  Input/Output Project"""
import sys
from os.path import exists

load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file


def add_arguments():
    """
    Save arguments from command line in list
    but check if file exists first so as not to overwrite
    args:
        sys.argv[1:]
    """
    if exists("add_item.json"):
        argument = load_from_json_file("add_item.json")
    else:
        argument = []

    for args in sys.argv[1:]:
        argument.append(args)

    save_to_json_file(argument, "add_item.json")

    loaded_objects = load_from_json_file("add_item.json")

    return loaded_objects


if __name__ == "__main__":
    add_arguments()
