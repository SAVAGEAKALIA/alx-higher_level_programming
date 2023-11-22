#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    n = 0
    try:
        for num in range(x):
            if type(my_list[num]) is int:
                print("{:d}".format(my_list[num]), end="")
                n += 1
    except OSError:
        raise IndexError
    else:
        print()
        return n
