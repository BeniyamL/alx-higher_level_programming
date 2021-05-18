#!/usr/bin/python3
class Node:
    """ a node class to define atributes and methods of a node """

    def __init__(self, data, next_node=None):
        """ function to initialize the node class

        Arguments:
           data: the data of the node
           next_node: the next node
        Returns:
           nothing
        """

        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        """ getter function of data

        Arguments:
           nothing
        Returns:
            the data of the node
        """
        return self.__data

    @data.setter
    def data(self, value):
        """ setter function to update the data of the node

        Arguments:
            value: the value we are going to set
        Returns:
            nothing
        """
        if type(value) is not int:
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """ getter function of next node

        Arguments:
           nothing
        Returns:
            the next node
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """ setter function to update the next node

        Arguments:
            value: the value we are going to set
        Returns:
            nothing
        """
        if type(value) is not Node and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """ function to define singly linked list"""

    def __init__(self):
        """ function to initialize singly linked list

        Arguments:
            nothing
        Returns:
            nothing
        """
        self.__head = None

    def __str__(self):
        """ print representation of the class singly linked list

        Arguments:
            nothing
        Returns:
            a list containing values of the single linked list
        """
        result = []
        cur = self.__head
        while cur is not None:
            result.append(str(cur.data))
            cur = cur.next_node
        return ("\n".join(result))

    def sorted_insert(self, value):
        """ function to insert a node in the increasing order

        Arguments:
            value: the value to be inserted
        Returns:
            nothing
        """
        new_node = Node(value)
        cur = self.__head
        if cur is None:
            new_node.next_node = None
            self.__head = new_node
        elif cur.data > value:
            new_node.next_node = cur
            self.__head = new_node
        else:
            while cur.next_node is not None and value > cur.next_node.data:
                cur = cur.next_node
            new_node.next_node = cur.next_node
            cur.next_node = new_node
