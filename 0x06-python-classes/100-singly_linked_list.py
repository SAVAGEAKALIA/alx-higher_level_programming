#!/usr/bin/python3
""" This module defines singly linked list in OOP """

class Node:
    """ Creates A Node for Singly linked list """

    def __init__(self, data, next_node=None):
        """ Initializes the data to be stored in Node
        data must be an integer """

        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """ Getter to return data  to class Node """
        return self.__data
    
    @data.setter
    def data(self, value):
        """ Value to be stored in Data
        value must be an integer """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        """ Getter to return next node in singly linked list """
        return self.__next_node
    @next_node.setter
    def next_node(self, value):
        """ Update next node in the singly linked list """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value


class SinglyLinkedList:
    """ A singly linked list Class """

    def __init__(self):
        """ Initialize an empty list
        Print out the entire list in stdout """
        self.__head = None

    def sorted_insert(self, value):
        """ Insert Node in the correct order """
        new_node = Node(value)
        if self.__head is None or self.__head.data > value:
            new_node.next_node = self.__head
            self.__head = new_node
            return

        current = self.__head
        while current.next_node is not None and current.next_node.data < value:
            current = current.next_node

        new_node.next_node = current.next_node
        current.next_node = new_node

    def print_list(self):
        tmp = ""
        current = self.__head
        while current is not None:
            tmp += f"{current.data}\n"
            current = current.next_node

        return  tmp

    def __str__(self):
        """ Override the __str__ method to print the linked list """
        return self.print_list()
