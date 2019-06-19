"""
Linear data structures
Stacks implementation in python3
"""
from node_implementation import Node #this library can be found in this very repository

#defining exception raised when we try to push data on an already full stack
class StackOverflow(Exception):
    "StackOverflow error: there's no more room to push data"

#defining exception raised when trying to pop from an empty stack
class StackUnderflow(Exception):
    "StackUnderflow error: this stack is already empty"

class Stack:

    #giving the faculty to set a stack's limit while instantiating
    def __init__(self, limit=None):
        self.limit = limit
        self.size = 0
        self.top = None

    #giving stack a string representation
    def __str__(self):
        return "A stack with size {size} and limit {limit}".format(size=self.size, limit=self.limit)

    #check whether stack is empty
    def is_empty(self):
        return self.size == 0

    #check whether a stack has room
    def has_room(self):
        if self.limit:
            return self.size < self.limit
        return True

    #push data on stack's top
    def push(self, data):
        if self.has_room():
            new_top = Node(data)
            new_top.set_link(self.top)
            self.top = new_top
            self.size += 1
        else:
            raise StackOverflow

    #return top node's data
    def peek(self):
        if self.is_empty():
            print("Stack is empty")
        else:
            return self.top.data

    #peek and remove top node
    def pop(self):
        if self.is_empty():
            raise StackUnderflow
        former_top = self.top
        self.top = former_top.next_node
        self.size -= 1
        return former_top.data