#!/usr/bin/python3
"""File for the Input/Output Project"""


def write_file(filename="", text=""):
    """
    Writes a text file (UTF8) and returns the number of characters written.

    Args:
        filename (str): The name of the file to write to.
        text (str): The text to be written to the file.

    Returns:
        int: The number of characters written to the file.
    """
    with open(filename, mode='w', encoding='utf-8') as f:
        chars_written = f.write(text)
        return chars_written
