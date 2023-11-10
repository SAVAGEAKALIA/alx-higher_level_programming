#!/usr/bin/python3
def search_replace(my_list, search, replace):
    h = []
    new_list = my_list.copy()
    for x in new_list:
        if x+1 is search:
            del new_list[x]
            new_list.insert(x, replace)
            return new_list
