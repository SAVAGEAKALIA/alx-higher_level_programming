#!/usr/bin/python3
import sys
def safe_function(fct, *args):
    try:
        return fct(*args)
    except Exception as val:
        print("Exception: {}".format(val), file=sys.stderr)
        return None
