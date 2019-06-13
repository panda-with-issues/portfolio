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
        return index // 2

    def get_left_child_index(self, index):
        return index * 2

    def get_right_child_index(self, index):
        return index * 2 + 1

    def has_child(self, index):
        return self.get_left_child_index(index) < len(self.dataset)

    """
    end helpers
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
        """#check whether data is a numeric data object
        if type(data) != int and type(data) != float and type(data) != str:
            raise TypeError"""
        #insert data
        self.dataset.append(data)
        #if there are more than one piece of data, heapify up
        if len(self.dataset) > 2:
            self.heapify_up()

    #sanitize the array pushing down the root untill it meets bigger children. When it's parent of two children, swap always with the smaller
    def heapify_down(self):
        parent_index = 1
        while self.has_child(parent_index):
            parent = self.dataset[parent_index]
            child_index = self.get_left_child_index(parent_index)
            child = self.dataset[child_index]
            #if there is a right child
            if child_index + 1 < len(self.dataset):
                right_child_index = self.get_right_child_index(parent_index)
                right_child = self.dataset[right_child_index]
                #if right child is bigger than left one, compare parent with it instead of comparing with left child
                if right_child < child:
                    child = right_child
                    child_index = right_child_index
            if parent > child:
                self.dataset[parent_index] = child
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
            self.dataset[1] = self.dataset[-1]
            self.dataset.pop()
            self.heapify_down()
            return root


class MaxHeap(MinHeap):
    #this class work exactly like the previous one, except in heapifying methods. Where the MinHeap makes comparisons between child and parent, MaxhHeap changes the
    #comparison's direction: greater becomes lesser and viceversa.

    def __str__(self):
        return "A maximum heap"

    def heapify_up(self):
        child_index = len(self.dataset) - 1
        while child_index > 1:
            child = self.dataset[child_index]
            parent_index = self.get_parent_index(child_index)
            parent = self.dataset[parent_index]
            if child > parent:
                self.dataset[child_index] = parent
                self.dataset[parent_index] = child
                child_index = parent_index
            else:
                break

    def heapify_down(self):
        parent_index = 1
        while self.has_child(parent_index):
            parent = self.dataset[parent_index]
            child_index = self.get_left_child_index(parent_index)
            child = self.dataset[child_index]
            if child_index + 1 < len(self.dataset):
                right_child_index = self.get_right_child_index(parent_index)
                right_child = self.dataset[right_child_index]
                if right_child > child:
                    child = right_child
                    child_index = right_child_index
            if parent < child:
                self.dataset[parent_index] = child
                self.dataset[child_index] = parent
                parent_index = child_index
            else:
                break