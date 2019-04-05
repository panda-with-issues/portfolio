"""
Tower of Hanoi
Practicing stacks with python3
"""

from stack_implementation import Stack #this library can be found in this very repository

class Hanoi_stack(Stack):

    #updating the constructor
    def __init__(self, position, limit=None):
        super().__init__(limit)
        self.position = position

    #overwriting string representation
    def __str__(self):
        chunks = [" ", "#", "-"]
        stack_chunked = []

        #get size of each disk currently on stack plus floor length
        disks_lengths = [2 * i + 1 for i in range(self.size+1)]

        #draw the stack
        for length in disks_lengths:

            #draw disks
            if length != disks_lengths[-1]:
                disk_structure = []
                n_blanks_per_part = int((disks_lengths[-1] - length) / 2)
                disk_structure.append(n_blanks_per_part)
                disk_structure.append(length)
                disk_structure.append(n_blanks_per_part)
                disk_chunked = []
                for i in range(len(disk_structure)):
                    if i % 2 == 0:
                        for blank in range(disk_structure[i]):
                            disk_chunked.append(chunks[0])
                    else:
                        for unit in range(disk_structure[i]):
                            disk_chunked.append(chunks[1])
                disk_strfd = "".join(disk_chunked)
                stack_chunked.append(disk_strfd)
            
            #draw the floor
            else:
                floor_chuncked = []
                for tile in range(length):
                    floor_chuncked.append(chunks[2])
                floor_strfd = "".join(floor_chuncked)
                stack_chunked.append(floor_strfd)

        stack_strfd = "\n".join(stack_chunked)
        return stack_strfd

"""
setting up the game
"""

left_stack = Hanoi_stack("left")
middle_stack = Hanoi_stack("middle")
right_stack = Hanoi_stack("right")

stacks = []
stacks.append(left_stack)
stacks.append(middle_stack)
stacks.append(right_stack)

#ask user how many disks they want to play with
while True:
    try:
        disks = int(input("How many disks do you want to play with? ").strip())
    except ValueError:
        print("Only integer numbers are allowed")
        continue
    if disks > 2:
        break
    else:
        print("Please enter a number greater than 2")

#placing disks on left stack
for i in range(disks, 0, -1):
    left_stack.push(i)
print(left_stack.peek(), left_stack.size)

#prompting the optimal number of moves to solve the game
n_optimal_moves = 2 ** disks - 1
print("\nThe fastest way you can solve this game is in {} moves\n\n".format(n_optimal_moves))

#ask user which stack they want to choose
def get_stack():
    valid_input = [stack.position[0] for stack in stacks]
    while True:
        user_input = input(" ").lower().strip()
        if user_input in valid_input:
            for stack in stacks:
                if user_input == stack.position[0]:
                    return stack
        else:
            for stack in stacks:
                print("Enter {letter} for {position} stack".format(letter=stack.position[0], position=stack.position))
            continue

#print current stack status
def print_screen():
    strfy = []
    for stack in stacks:
        strfy.append(stack.__str__())
    strfd = "".join(strfy)
    print(strfd)

"""
Start game routine
"""

n_moves = 0

#game ends if right stack is full
while right_stack.size < disks:

    #prompt stacks
    print_screen()

    #set turn routine
    while True:
        print("Take a disk from: ")
        from_stack = get_stack()
        #validating move
        if from_stack.is_empty():
            print("There's nothing to pick there")
            continue
        while from_stack:
            print("And move it to: ")
            to_stack = get_stack()
            if 
