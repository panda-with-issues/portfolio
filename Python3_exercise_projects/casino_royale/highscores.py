import csv
from math import log2, inf

class DictHeap:
    # keep track of the maximum element of a dict. Elements are sorted by the value stored in ordering_key, which is passed at instantiation

    def __init__(self, ordering_key, max_len):
        self.dataset = []
        self.ordering_key = ordering_key
        self.max_len = max_len

    def push(self, element):
        self.dataset.append(element)
        self.heapify_up()

        while len(self.dataset) > self.max_len:
            tree_level = int(log2(len(self.dataset)))
            first_element_of_level = 2**tree_level - 1
            self.dataset, lines_to_check = self.dataset[:first_element_of_level], self.dataset[first_element_of_level:]
            min = inf
            to_remove = None
            for line in lines_to_check:
                if int(line[self.ordering_key]) < min:
                    min = int(line[self.ordering_key])
                    to_remove = line
            lines_to_check.remove(to_remove)
            for line in lines_to_check:
                self.push(line)

    def get_parent_index(self, child_index):
        if child_index == 1 or child_index == 2:
            return 0

        if child_index % 2 == 1:
            return child_index // 2

        else:
            return (child_index - 1) // 2

    def get_lesser_child_index(self, parent_index):
        if parent_index == 0:
            possible_left_child_index = 1
            possible_right_child_index = 2

        else:
            possible_left_child_index = parent_index * 2 + 1
            possible_right_child_index = possible_left_child_index + 1

        acceptable_threshold = len(self.dataset) - 1

        if possible_left_child_index <= acceptable_threshold:
            left_child = self.dataset[possible_left_child_index]
        else:
            return

        if possible_right_child_index <= acceptable_threshold:
            right_child = self.dataset[possible_right_child_index]
            if int(right_child[self.ordering_key]) > int(left_child[self.ordering_key]):
                return possible_right_child_index
        
        return possible_left_child_index

    def heapify_up(self, child_index=None):
        if child_index is None:
            child_index = len(self.dataset) - 1

        # base case
        if child_index == 0:
            return

        child = self.dataset[child_index]
        parent_index = self.get_parent_index(child_index)
        parent = self.dataset[parent_index]
        if int(child[self.ordering_key]) > int(parent[self.ordering_key]):
            self.dataset[child_index], self.dataset[parent_index] = self.dataset[parent_index], self.dataset[child_index]
            self.heapify_up(parent_index)
    
    def pop(self):
        self.dataset[0], self.dataset[-1] = self.dataset[-1], self.dataset[0]
        element_to_return = self.dataset.pop()
        self.heapify_down()
        return element_to_return

    def heapify_down(self, parent_index=None):
        if parent_index is None:
            parent_index = 0

        child_index = self.get_lesser_child_index(parent_index)

        if child_index is None:
            return

        parent = self.dataset[parent_index]
        child = self.dataset[child_index]
        if int(child[self.ordering_key]) > int(parent[self.ordering_key]):
            self.dataset[parent_index], self.dataset[child_index] = self.dataset[child_index], self.dataset[parent_index]
            self.heapify_down(child_index)


labels = ['current', 'position', 'name', 'coins'] # current is a token ('>') used to quickly identify on the board the current session score
lines_dumper = DictHeap('coins', 8) # here will be stored the content of highscore.csv, so it can be modified and manipulated before beeing wrote into the output file
                                     # The len of this dumper is binded to DictHeap.len_max, so there are very few elements to save in memory: thus we can afford this
                                     # behaviour without excessive fear.
                                     # If you are wondering why I didn't use a database to easily accomplish this task, the answer is simple: I have no idea on how
                                     # db works and how to use them in Python3 :D

def add_line_to_dumper(name, coins, dumper=lines_dumper, labels=labels): # ** is a dictionary with player's name and their coins at the end of the game
    new_values = ['>', None, name, coins]
    new_line = {key:value for key, value in zip(labels, new_values)}
    dumper.push(new_line)

def generate_highscore_csv(name, coins):  
    try:
        with open('.highscores.csv', 'r') as file:
            input_file = csv.DictReader(file)
            for line in input_file:
                # clean the line getting rid of the former current token
                if line['current'] == '>':
                    line['current'] = ''
                lines_dumper.push(line)
                        
    except FileNotFoundError:
        # this can't be avoided, because the 'r+' mode doesn't create a new file if the passed one is not found. With the 'a+' mode, in th other hand, you can read only
        # what you have just wrote. Because the file needs to be dumped before it is truncated and re-written, the only way is to handle the FileNotFound exception
        # with this poor try-catch block
        pass
        
    with open('.highscores.csv', 'w') as file:
        output = csv.DictWriter(file, fieldnames=labels)
        output.writeheader()
        add_line_to_dumper(name, coins)
        # add ranks to highscores
        i = 1
        while lines_dumper.dataset:
            clean_line = lines_dumper.pop()
            clean_line['position'] = i
            output.writerow(clean_line)
            i += 1