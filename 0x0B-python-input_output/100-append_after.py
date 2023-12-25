#!/usr/bin/python3
""" File for the  Input/Output Project"""


def append_after(filename="", search_string="", new_string=""):
    """
    Inserts a line of text after each line containing a specific string in a file.

    Args:
        filename (str): The name of the file.
        search_string (str): The string to search for in each line.
        new_string (str): The line of text to insert after each matching line.
    """

    # Open the file in read mode
    with open(filename, mode='r', encoding='utf-8') as file:
        # Read all lines from the file
        lines = file.readlines()

    # Open the file in write mode to overwrite it
    with open(filename, mode='w', encoding='utf-8') as file:
        for line in lines:
            file.write(line)  # Write the original line to the file
            if search_string in line:
                file.write(new_string)  # Write the new line after the matching line
