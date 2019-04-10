"""
Complex Data Structures
Hash maps implementation in python3
-----------------------------------
Disclaimer: in Python we don’t have an array data structure that uses a contiguous block of memory. So I'll simulate an array by creating
a list and keeping track of its size with an additional variable. 
This is somewhat elaborate for the actual storage of a key-value pair, but hey, this is just an exercise to gain a deeper understanding
of the structure as it is constructed.
For real-world use cases in which a key-value store is needed, Python offers a built-in hash table implementation with dictionaries.
"""

from linked_list_implementation import Linked_list

class HashMap:

    #define the size of the array while instantiating the hash map
    def __init__(self, array_size):
        self.array_size = array_size
        #create the array with given size
        self.array = [None for i in range(self.array_size)]
        #prevent to hash same keys with different values in case of memory expansion
        self.buffer = 0
        self.size = self.array_size - self.array.count(None)

    #defining the hashing function
    def hash(self, key):
        
        #check if the key is hashable
        if type(key) != list and type(key) != dict and key != "deleted":
            
            if type(key) == tuple:
                hash_code = 0
                for data in key:
                    if type(data) == str:
                        hash_code += sum(data.encode())
                    elif type(data) == float:
                        hash_code += int(data)
                    else:
                        hash_code += data
            elif type(key) == str:
                hash_code = sum(key.encode())
            elif type(key) == float:
                hash_code = int(key)
            else:
                hash_code = key
            
            return hash_code % (self.array_size - self.buffer)

        raise TypeError

 #expand memory if trying to insert data into a full array
    def expand_memory(self, index):
        for i in range(index):
            self.array.append(None)
            self.array_size += 1
            self.buffer += 1
        
    #defining a squared probing for open addressng and expand memory if doing too many iterations
    def sqrd_probing(self, index, key, inserting=True):
        i = 0
        while self.array[index] != None:
            if i >= 50 and inserting:
                self.expand_memory(index)
            if self.array[index][0] == key:
                return index
            if self.array[index] == "deleted" and inserting:
                return index
            i += 1
            probing = i ** 2
            index += probing
            if index >= self.array_size:
                if i < 50:
                    index %= (self.array_size - self.buffer)
                else:
                    index %= self.array_size
        return index

    #allocate data in the array
    def insert(self, key, data):
        index = self.hash(key)
        bucket = self.array[index]
        data_to_insert = [key, data]

        #handling collisions using a linked list separate chaining for array smaller than 10
            # 10 was chosen merely for its ease in debugging
        if self.array_size < 10:
            
            if bucket == None:
                self.array[index] = Linked_list(data_to_insert)
                self.size += 1
        
            else:
                current_node = bucket.head_node
                while current_node:
                    data_stored = current_node.data
                    if data_stored[0] == key:
                        data_stored[1] = data
                        break
                    if current_node.next_node == None:
                        bucket.add_node(data_to_insert)
                        self.size += 1
                    current_node = current_node.next_node
                    
        #handling collisions using a squared probing for longer arrays
            # Obiouvsly, 10 is a too little value to open address with a squared probing.
            # However I chose to implement square probing just to try and see if I was able to.
            # Neither open addressing nor squared probing are efficient in this scenario, but they serve the purpose of practicing and understanding.
        else:
            if self.size == len(self.array):
                self.expand_memory(index)
            elif self.array[index] == None or self.array[index] == "deleted":
                self.array[index] = data_to_insert
                self.size += 1
            else:
                new_index = self.sqrd_probing(index, key)
                if self.array[new_index] == None or self.array[new_index] == "deleted":
                    self.array[new_index] = data_to_insert
                    self.size += 1
                else:
                    self.array[new_index][1] = data
                
    #retrieve data given the key
    def get(self, key):
        index = self.hash(key)

        if type(self.array[index]) == Linked_list:
            current_node = self.array[index].head_node
            while current_node:
                if current_node.data[0] == key:
                    return current_node.data[1]
                current_node = current_node.next_node
            raise KeyError

        else:
            key_val_pair = self.array[index]
            if key_val_pair[0] == key:
                return key_val_pair[1]
            else:
                new_index = self.sqrd_probing(index, key, False)
                key_val_pair = self.array[new_index]
                if key_val_pair == None or key_val_pair == "deleted":
                    raise KeyError
                return key_val_pair[1]

    #delete the pair given the key
    def pop(self, key):
        data_to_remove = [key, self.get(key)] #here is where the key check is done
        index = self.array.index(data_to_remove)
        if type(self.array[index]) == Linked_list:
            self.array[index].remove_node(data_to_remove)
            self.size -= 1
        elif self.array[index] == data_to_remove:
            self.array[index] = "deleted"
            self.size -= 1
        else:
            new_index = self.sqrd_probing(index, key, True)
            self.array[new_index] = "deleted"
            self.size -= 1