"""
Linear data structure
Queues implementation in Python3
"""

from node_implementation import Node #this library can be found in this very repository

#defining new exceptions
class QueueUnderflow(Exception):
    "QueueUnderflow error: there's nothing here to be dequeued"

class QueueOverflow(Exception):
    "QueueOverflow error: there's no more room for data in this queue"

class Queue:

    #giving the faculty to set a limit and enqueue the first node while instantiating
    def __init__(self, first_node=None, limit=None):
        self.limit = limit
        self.head = None
        self.tail = None
        self.size = 0
        if first_node:
            self.enqueue(first_node)

    #giving a string representation
    def __str__(self):
        unbounded = "A queue of size {}, ".format(self.size)
        bounded = "A bounded queue of size {size} on {limit}, ".format(size=self.size, limit=self.limit)
        last_part = "with head {head_data} and tail {tail_data}".format(head_data=self.head.data, tail_data=self.tail.data)
        if self.limit:
            return bounded + last_part
        return unbounded + last_part

    #check if queue is empty
    def is_empty(self):
        return self.size == 0

    #check if a bounded queue has room for more data
    def has_room(self):
        if self.limit:
            return self.size < self.limit
        return True

    #return head's data
    def peek(self):
        if self.is_empty():
            return "Nothing in queue"
        return self.head.data

    #add data at the tail of the queue
    def enqueue(self, data):
        if self.has_room():
            new_node = Node(data)
            if self.is_empty():
                self.head = new_node
                self.tail = new_node
            else:
                self.tail.set_link(new_node)
                self.tail = new_node
            self.size += 1
        else:
            raise QueueOverflow

    #peek and remove queue's head
    def dequeue(self):
        if self.is_empty():
            raise QueueUnderflow
        dequeued = self.head
        self.head = self.head.next_node
        if self.size == 1:
            self.tail = None
        self.size -= 1
        return dequeued.datag