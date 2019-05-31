"""
Sorting Algorithms in Python
"""

from random import randrange

"""
Bubble Sort
"""

# With this algorithm, we take the first value of the list and compare it with its next element. If the element is greater than its next, we swap their values. This routine must be repeated N times, where N
# is the list's length

def bubble_sort(lst):

    for i in range(len(lst)):

        # because at every iteration the biggest number is placed in the rightmost free space, we can optimize the algorithm by excluding the last i elements at every loop
        # Even with this expedient, however, the algorithm runtime is still O(N^2)
        for idx in range(len(lst) - 1 - i):
            if lst[idx] > lst[idx + 1]:
                lst[idx], lst[idx+1] = lst[idx+1], lst[idx]

"""
Merge Sort
"""

# this algorithm works splitting in half the array untill the subarrays contain at most one element. Then it compare the leftmost element of an array with the leftmost of the
# next one and merges the subarrays into ordered subarrays, untill the original lenght is reached. The runtime of this algorithm is always O(NlogN)

#First we recursively split the list in subarrays that conteins at most 1 element
def merge_sort(lst):
    
    #base case: the subarray contains at most 1 element
    if len(lst) <= 1:
        return lst

    #inductive step: if the base case is not met, split in halves the list
    middle_idx = len(lst) // 2
    left_list = lst[:middle_idx]
    right_list = lst[middle_idx:]

    #recursive step: call the function on the halves until they meet the base case
    ready_to_sort_left = merge_sort(left_list)
    ready_to_sort_right = merge_sort(right_list)

    return merge(ready_to_sort_left, ready_to_sort_right)

#Then we merge the sublist ordering the elements
def merge(left_list, right_list):
    
    sorted = []

    while left_list and right_list:
        if left_list[0] < right_list[0]:
            sorted.append(left_list.pop(0))
        else:
            sorted.append(right_list.pop(0))

    if left_list:
        sorted += left_list

    if right_list:
        sorted += right_list

    return sorted

"""
Quicksort
"""

# In quicksort first we choose a pivot against which every other element will be compared. We then partition the list into 3 subarray, one containing all the element lesser
# than the pivot, one with the pivot and the last one with every element greater than pivot. This comparation is recursively repeated untill subarrays contain at most one
# element. The runtime of this algorithm is in average O(NlogN)

# we will use pointers to iterate through the list
def quicksort(lst, start, end):

    # base case: subarray contains at most 1 element
    if start >= end:
        return lst

    # inductive case: we choose a random pivot element
    pivot_idx = randrange(0, end+1)

    # now we swap elements in order to have in the leftmost place every value lesser than the pivot and viceversa. We swap the pivot with last element so we can always find it
    # later
    lst[end], lst[pivot_idx] = lst[pivot_idx], lst[end]

    # we will use two pointer to rearrange the values in the list. The first pointer keep track of the current digit in the loop, the second will keep track of the leftmost
    # position where we can allocate data

    leftmost_idx = 0
    current_idx = 0

    while current_idx < end:
        if lst[current_idx] < lst[end]:
            lst[current_idx], lst[leftmost_idx] = lst[leftmost_idx], lst[current_idx]
            leftmost_idx += 1
        current_idx += 1
    
    #after having traversed the array, swap the pivot with the leftmost pointer: in this way we have partitioned the array
    lst[leftmost_idx], lst[end] = lst[end], lst[leftmost_idx]
    
    #recursive step: function is called on left and right sublist untill they meet the base case
    return quicksort(lst, start, leftmost_idx-1), quicksort(lst, leftmost_idx+1, end)

"""
Radix sort
"""

# Radix sort sorts element by comparing every i-th digit of every element untill every digit is been checked. Elements are placed in ten buckets, one for every digit, and
# rearranged at every traverse. We will implement this algorithm with the LSD variant, that is starting our sorting by the rightmost digit. This method doesn't use comparisons
# and has the quickest runtime with O(N) 

def radix_sort(lst):

    exp = 0
    ordered_lst = lst.copy()

    while True:
        
        buckets = [[] for i in range(10)]

        # we place elements into the proper bucket basing of the digit we are considering
        for element in ordered_lst:
            element_clean = element // 10**exp
            last_digit = element_clean % 10
            buckets[last_digit].append(element)

        # we then reorder the list following the buckets
        ordered_lst = []
        for i in range(10):
            ordered_lst += buckets[i]
        
        # if every element is in 0's bucket, we reached the end of the algorithm
        if len(buckets[0]) == len(lst):
            return ordered_lst

        # else we empty the buckets and check the next digit to the left
        else:
            exp += 1

"""
DEBUG
"""

unsorted = [randrange(0, 501) for i in range(11)]
print(unsorted)
quicksort(unsorted, 0, len(unsorted) - 1)
print(unsorted)
