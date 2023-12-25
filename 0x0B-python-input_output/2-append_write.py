#!/usr/bin/python3
"""File for the Input/Output Project"""


def append_write(filename="", text=""):
    """
    Appends a text file (UTF8) and returns the number of characters written.

    Args:
        filename (str): The name of the file to write to.
        text (str): The text to be apppended to the file.

    Returns:
        int: The number of characters appended to the file.
    """
    with open(filename, mode='a', encoding='utf-8') as f:
        chars_append = f.write(text)
        return chars_append
