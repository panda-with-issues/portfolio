"""
Linear data structures
Linked list implementation in python3
"""

from node_implementation import Node #this library can be found in the same repositoryof this code

class Linked_list:

    #giving the faculty to set the head node while instantiating the list
    def __init__(self, head=None):
        self.head_node = Node(head)

    #add a new head node
    def set_new_head(self, data):
        new_head = Node(data)
        new_head.set_link(self.head_node)
        self.head_node = new_head

    #adds a new node in the end of the list
    def add_node(self, data):
        current_node = self.head_node
        while current_node:
            if current_node.next_node == None:
                current_node.next_node = Node(data)
                break
            current_node = current_node.next_node

    #returns a printable string made of values of each node in the linked list
    def strfy(self):
        string = ''
        current_node = self.head_node
        while current_node:
            string += str(current_node.data)
            if current_node.next_node == None:
                return string
            string += ' -> '
            current_node = current_node.next_node

    #removes the first node found with given data
    def remove_node(self, data_to_remove):
        if self.head_node.data == data_to_remove:
            self.head_node = self.head_node.next_node
        else:
            current_node = self.head_node
            while current_node:
                if current_node.next_node == None:
                    break
                if current_node.next_node.data == data_to_remove:
                    current_node.set_link(current_node.next_node.next_node)
                    break
                current_node = current_node.next_node

    #removes any node with given data
    def remove_all(self, data_to_remove):
        if self.head_node.data == data_to_remove:
            self.head_node = self.head_node.next_node
        current_node = self.head_node
        while current_node:
            if current_node.next_node == None:
                break
            if current_node.next_node.data == data_to_remove:
                new_next = current_node.next_node.next_node
                while new_next != None and new_next.data == data_to_remove:
                    new_next = new_next.next_node
                current_node.set_link(new_next)
            current_node = current_node.next_node

    #reverses list
    def reverse(self):
        current_node = self.head_node
        nodes = []
        while current_node:
            print(nodes)
            nodes.append(current_node)
            current_node = current_node.next_node
        nodes.reverse()
        self.head_node = nodes[0]
        for i in range(len(nodes)):
            if i == len(nodes) - 1:
                nodes[i].set_link(None)
            else:
                nodes[i].set_link(nodes[i+1])