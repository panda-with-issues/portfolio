"""
Linear data structures
Node implementation in python3
"""

class Node:

    #defining class' constructor and string representation

    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node #defines the node referred by the current one. Default value is none

    def __repr__(self):
        return "A node with data: {}.".format(self.data)

    #defining class' methods

    #get node's data
    def get_data(self):
        return self.data

    #get node pointed
    def get_next(self):
        return self.next_node

    #set pointer
    def set_link(self, next_node):
        self.next_node = next_node