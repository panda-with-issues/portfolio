"""
Complex Data Structures
Hash maps implementation in python3
-----------------------------------
Disclaimer: in Python we don’t have an array data structure that uses a contiguous block of memory. So I'll simulate an array by creating
a list and keeping track of its size with an additional variable. 
This is somewhat elaborate for the actual storage of a key-value pair, but hey, this is just an exercice to gain a deeper understanding
of the structure as it is constructed.
For real-world use cases in which a key-value store is needed, Python offers a built-in hash table implementation with dictionaries.
"""

from linked_list_implementation import Linked_list

class LinkedList(Linked_list):

    def __str__(self):
        return self.strfy()
    
    #making list iterable in nodes's data
    def __iter__(self):
        data = []
        i = self.head_node
        while i:
            data.append(i.data)
            i = i.next_node
        return data

class HashMap:

    #define the size of the array while instantiating the hash map
    def __init__(self, array_size):
        self.array_size = array_size
        #create the array with given size
        self.array = [None for i in range(self.array_size)]

    #defining the hashing function
    def hash(self, key):
        
        #check if the key is hashable
        if type(key) == int or type(key) == str:

            if type(key) == str:
                hash_code = sum(key.encode())
            else:
                hash_code = key
            return hash_code % self.array_size

        raise TypeError

    #defining a squared probing for open addressng
    def sqrd_probing(self, index):
        i = 0
        while self.array[index] == None:
            i += 1
            probing = i ** 2
            index += probing
            if index > self.array_size:
                index %= self.array_size
        return index

    #allocate data in the array
    def insert(self, key, data):
        index = self.hash(key)
        bucket = self.array[index]

        if self.array[index] == None:
            self.array[index] = [key, data]

        #handling collisions using a linked list separate chaining for array smaller than 16
        elif self.array_size <= 16:
            if type(self.array[index]) != LinkedList:
                ll = LinkedList(self.array[index])
                self.array[index] = ll
            ll.add_node([key, data])

        #handling collisions using a squared probing for longer arrays
        else:
            index = self.sqrd_probing(index)
            self.array[index] = [key, data]

    #retrieve data given the key
    def get(self, key):
        index = self.hash(key)

        if type(self.array[index]) == LinkedList:
            i = self.array[index].head_node
            data = []
            while i:
                print(i)
                data.append(i.data)
                i = i.next_node
                print(data)
            for pairs in data:
                if pairs[0] == key:
                    return pairs[1]

        else:
            bucket = self.array[index]
            while bucket[0] == key:
                index = self.sqrd_probing(index)
            return bucket[1]




ll_map = HashMap(4)
ll_map.insert("Sailor Moon", "Tsukino Usagi")
ll_map.insert("Sailor Mercury", "Mizuno Ami")
ll_map.insert("Sailor Mars", "Hino Rei")
ll_map.insert("Sailor Jupiter", "Kino Makoto")
ll_map.insert("Sailor Venus", "Aino Minako")
"""
print(ll_map.array)
print(ll_map.array[1])
print(ll_map.array[3])
"""

print(ll_map.get("Sailor Moon"))
#print(ll_map.get("Sailor Jupiter"))