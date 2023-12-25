#!/usr/bin/python3
""" File for the  Input/Output Project"""


def read_file(filename=""):
    """Reads a text file (UTF8) and prints it to stdout."""
    with open(filename, mode='r', encoding='utf-8') as f:
        for line in f:
            print(line, end="")
