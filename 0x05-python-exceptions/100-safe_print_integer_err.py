#!/usr/bin/python3
import sys
def safe_print_integer_err(value):
    try:
        # Try to print the integer value
        print("{:d}".format(value))
        return True
    except Exception as str:
        # Handle the error if the value is not an integer
        #valu = "Exception: Unknown format code 'd' for object of type 'str'"
        print("Exception: {}".format(str), file=sys.stderr)
        return False
