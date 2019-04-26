"""
Complex data structures
Heaps implementation in python3
"""
"""
Heaps are figured and handled as if they were binary tree. Though because of efficiency, the underlaying data structure will be a list (arrays are not an option in python).
Converting the relationship between parents and childs in list's indices is a matter of plain arithmetic and will be handled with dedicated helper methods.
In order to keep things simpler, the list will have a sentinel element at index 0. This element will handle the possible IndexErrors and will make the root node easier
accessible keeping it at index 1.
Because this is an exercise, I will implement a minimum and a maximum heaps working only with numbers.
"""

class MinHeap:

    def __init__(self):
        self.dataset = [None]

    """
    helper methods
    """

    def get_parent_index(self, index):
        parent_index = index // 2
        return parent_index

    def get_left_child_index(self, index):
        child_index = index * 2
        return child_index

    def get_right_child_index(self, index):
        child_index = index * 2 + 1
        return child_index

    """
    end helper
    """

    #sanitize heap when updating the dataset keeping children greater than parents
    def heapify_up(self):
        child_index = len(self.dataset) - 1
        while child_index > 1:
            child = self.dataset[child_index]
            parent_index = self.get_parent_index(child_index)
            parent = self.dataset[parent_index]
            if child < parent:
                self.dataset[parent_index] = child
                self.dataset[child_index] = parent
                child_index = parent_index
            else:
                break

    #add data to dataset and sanitize array heapifying up
    def add(self, data):
        #check whether data is a numeric data object
        if type(data) != int and type(data) != float:
            raise TypeError
        #insert data
        self.dataset.append(data)
        #if there are more than one piece of data, heapify up
        if len(self.dataset) > 2:
            self.heapify_up()
        print(self.dataset)

"""
debug
"""
mucchio = MinHeap()
from random import randrange
for i in range(10):
    mucchio.add(randrange(0,31))
print(mucchio.dataset)
