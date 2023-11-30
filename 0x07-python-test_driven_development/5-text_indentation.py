#!/usr/bin/python3
"""
Write a function that prints a text with 2 new lines
after each of these characters: ., ? and :
"""


def text_indentation(text):
    """
    Function that prints text after
    these characters: ., ? and :
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    formatted_text = ""

    # Iterate through each character in the input text
    for delim in ".?:":
        text = (delim + "\n\n").join(
            [line.strip(" ") for line in text.split(delim)])

    # Remove any trailing new lines
    print(text.rstrip())
