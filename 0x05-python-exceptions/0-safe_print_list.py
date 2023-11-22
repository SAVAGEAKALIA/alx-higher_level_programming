#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        n = 0
        for num in my_list[:x]:
            print(num, end="")
            n += 1
        print()
        return n
    except (IndexError, TypeError, OSError):
        print()
        return n
