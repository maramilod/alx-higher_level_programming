#!/usr/bin/python3
"""hey"""


class Node:
    """node"""

    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """getter"""

        return self.__data

    @data.setter
    def data(self, val):
        if not isinstance(val, int):
            raise TypeError("data must be an integer")
        self.__data = val

    @property
    def next_node(self):
        """getter"""

        return self.__next_node

    @next_node.setter
    def next_node(self, val):
        if not isinstance(val, Node) and val is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = val


class SinglyLinkedList:
    """define a singaly linked list"""

    __head = None

    def __init__(self):
        """pass"""

        pass

    def __str__(self):
        """pos..."""

        if self.__head is None:
            return ''
        tmp = self.__head
        string = ''
        while tmp.next_node is not None:
            string += str(tmp.data) + '\n'
            tmp = tmp.next_node
        return string + str(tmp.data)

    def sorted_insert(self, value):
        """stored"""

        if (self.__head is None or self.__head.data >= value):
            self.__head = Node(value, self.__head)
            return

        tmp = self.__head
        while tmp.next_node is not None and tmp.next_node.data < value:
            tmp = tmp.next_node
        tmp.next_node = Node(value, tmp.next_node)
