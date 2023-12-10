#!/usr/bin/python3
""" Python3 code list with Test """


class MyList(list):
    """ Class Object that inherits from list """

    def print_sorted(self):
        """ Prints a sorted list """
        sorted_list = self[:]
        sorted_list.sort()
        print("{}".format(sorted_list))
