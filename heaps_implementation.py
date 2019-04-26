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

    def __str__(self):
        return "A minimum heap"

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

    def has_child(self, data):
        data_index = self.dataset.index(data)
        return self.get_left_child_index(data_index) < len(self.dataset)

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

    #sanitize the array pushing down the root untill it meets bigger children. When it's parent of two children, swap always with the smaller
    def heapify_down(self):
        parent_index = 1
        while self.has_child(parent):
            parent = self.dataset[parent_index]
            child_index = self.get_left_child_index(parent_index)
            child = self.dataset[child_index]
            right_child_index = self.get_right_child_index(parent_index)
            #if there is a right child
            if left_child_index + 1 < len(self.dataset):
                right_child = self.dataset[right_child_index]
                #if right child is bigger than left one, compare parent with it instead of comparing with left child
                if right_child < left_child:
                    child = right_child
                    child_index = right_child_index
            if parent > child:
                self.dataset[parent] = child
                self.dataset[child_index] = parent
                parent_index = child_index
            else:
                break

             


    #remove and return the minimum value into the array. The last element of the list is put in its place. Then sanitize the array heapifing down
    def retrieve(self):
        #check whether there is anything to return
        if len(self.dataset) == 1:
            print("Heap is empty")
        else:
            root = self.dataset[1]
            new_root = self.dataset.pop()
            self.dataset[1] = new_root
            self.heapify_down()
            return root

"""
debug
"""
mucchio = MinHeap()
from random import randrange
for i in range(10):
    mucchio.add(randrange(0,31))
print(mucchio.dataset)
print(self.retrieve)
