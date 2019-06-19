"""
Search algorithms implementation in Python3
"""

# For the sake of this exercise, algorithmes will be implemented for being applied on a list of numbers and they'll return the index position of the target within the list.

"""
Linear Search
"""

# To find the target, this algorithm traverse the list element per element untill target is found or the list meets the end. If requested, the algorithm can search for
# duplicate values and return a list of indices.
# Linear search has runtime of O(N) and performes well on unordered lists or when we exspect to find the target among firsts element of our list.

def linear_search(lst, target, duplicate=False):

    if duplicate:
        positions = []
    
    for idx in range(len(lst)):
        if lst[idx] == target:
            if not duplicate:
                return idx
            else:
                positions.append(idx)

    if not duplicate:
        raise ValueError("Value searched is not in list")
        
    elif positions:
        return positions

    else:
        raise ValueError("Value searched is not in list")

"""
Binary Search
"""

# This algorithm is very efficient in finding the target, with a runtime of O(logN). Though it can be applied only on ordered lists.
# It works comparing the element at the middle index with the target. If values don't match, it splits the array in half and choose which half will be checked based on the 
# middle value being greater or lower than the target. It keeps splitting until the target is found or the half is empty.
# Binary Search will be implemented recursively with pointers

def binary_search(lst, target, start, end):

    middle_idx = (start + end) // 2

    #base cases: list is empty or target is found
    if start > end:
        raise ValueError("Value searched is not in list")
    if lst[middle_idx] == target:
        return middle_idx

    #recursive step: split the array in half moving pointers, basing on middle value's comparation against target and recall function on the chosen half
    if lst[middle_idx] > target:
        return binary_search(lst, target, start, middle_idx-1)

    else:
        return binary_search(lst, target, middle_idx+1, end)