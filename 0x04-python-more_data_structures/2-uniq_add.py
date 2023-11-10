#!/usr/bin/python3
def uniq_add(my_list=[]):
    new_list = set(my_list)
    add = 0
    for x in list(new_list):
        add += x
    return add
