#!/usr/bin/python3
""" Python class My int"""


class MyInt(int):
    """ Class MyInt that inherits from int """

    def __eq__(self, other):
        """ Inverts the == operator """
        return super().__ne__(other)

    def __ne__(self, other):
        """ Inverts the != operator """
        return super().__eq__(other)
