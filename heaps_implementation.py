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

    #when adding, always check whether the heap's property is satisfied (child must be greater than parent). If not, heapify up
    def add(self, data):
        #check whether data is a numeric data object
        if type(data) != int and type(data) != float:
            raise TypeError
        self.dataset.append(data)
        data_index = len(self.dataset) - 1
        parent_index = self.get_parent_index(data_index)
        

