#!/usr/bin/python3
def no_c(my_string):
    a = ""
    for x in my_string:
        if x not in 'cC':
            a += x
    return a
