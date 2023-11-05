#!/usr/bin/python3
import sys

if __name__ == "__main__":

    num_argv = len(sys.argv) - 1
    argv_list = sys.argv[1:]

    if num_argv == 0:
        print("0 argument")
    else:
        print("{} arguments".format(num_argv))

    for i, arg in enumerate(argv_list, 1):
        print("{}: {}".format(i, arg))
