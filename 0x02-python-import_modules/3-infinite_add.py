#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    argv_list = argv[1:]
    result = 0

    for arg in (argv_list):
        result += int(arg)

    print("{}".format(result))
