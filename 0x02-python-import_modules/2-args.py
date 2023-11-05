#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":

    num_argv = len(argv) - 1
    argv_list = argv[1:]

    if num_argv == 0:
        print("{} arguments.".format(num_argv))
    elif num_argv == 1:
        print("{} argument:".format(num_argv))
    else:
        print("{} arguments:".format(num_argv))

    for i, arg in enumerate(argv_list, 1):
        print("{}: {}".format(i, arg))
