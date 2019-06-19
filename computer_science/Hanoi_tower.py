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
        return "This is the {} stack".format(self.position)

    #making stack iterable
    def __iter__(self):
        iterable = []
        current_disk = self.top
        while current_disk:
            iterable.append(current_disk)
            current_disk = current_disk.next_node
        return iterable

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

#giving disks a visual representation
chunks =[" ", "#"]
disks_lengths = [2 * i + 1 for i in range(disks)]
disks_strfd = []
for disk in disks_lengths:
    disk_structure = []
    n_blanks_per_part = int((disks_lengths[-1] - disk) / 2) + 1
    disk_structure.append(n_blanks_per_part)
    disk_structure.append(disk)
    disk_structure.append(n_blanks_per_part)
    disk_chunked = []
    for index in range(len(disk_structure)):
        for i in range(disk_structure[index]):
            chunk = index % 2
            disk_chunked.append(chunks[chunk])
    disks_strfd.append("".join(disk_chunked))

#mapping each disk with its own visual representation
disk_to_visual = {disk.data:string for disk, string in zip(left_stack.__iter__(), disks_strfd)}
filler_chuncked = [chunks[0] for letter in disks_strfd[0]] #actually can be any index
ground_chuncked = ["-" for letter in disks_strfd[0]]
disk_to_visual.update({-1:"".join(filler_chuncked), 0:"".join(ground_chuncked)})

#print current stack status
def print_screen():
    
    levels = []

    max_level = 0
    for stack in stacks:
        if stack.size > max_level:
            max_level = stack.size
    
    for i in range(max_level, -1, -1):
        level_structure = []
        for stack in stacks:
            if i == 0:
                level_structure.append(disk_to_visual[0])
            elif stack.size > i:
                delta = stack.size - i
                disk_to_append = stack.top
                for ii in range(delta):
                    disk_to_append = disk_to_append.next_node
                level_structure.append(disk_to_visual[disk_to_append.data])
            elif stack.size == i:
                level_structure.append(disk_to_visual.get(stack.peek()))
            else:
                level_structure.append(disk_to_visual[-1])
        levels.append("".join(level_structure))
    
    for level in levels:
        print(level)

#prompting the optimal number of moves to solve the game
n_optimal_moves = 2 ** disks - 1
print("\nThe fastest way you can solve this game is in {} moves\n\n".format(n_optimal_moves))

#ask user which stack they want to choose. If anything is passed, allow user to redo previous choice
def get_stack(q=False):
    valid_input = [stack.position[0] for stack in stacks]
    if q:
        valid_input.append("q")
    while True:
        user_input = input("").lower().strip()
        if user_input in valid_input:
            if user_input == "q":
                return False
            for stack in stacks:
                if user_input == stack.position[0]:
                    return stack
        for stack in stacks:
            print("Enter {letter} for {position} stack".format(letter=stack.position[0], position=stack.position))
        if q:
            print("Enter q to pick from another stack")
        continue

"""
Start game routine
"""

n_moves = 0

#game ends if right stack is full
while right_stack.size < disks:

    #prompt stacks
    print("\n")
    print_screen()

    #set turn routine
    while True:

        #pick a disk
        print("\nWhere do you want to take the disk from? [l, m, r]:")
        from_stack = get_stack()

        #validating move
        if from_stack.is_empty():
            print("\nThere's nothing to pick up there")
            continue

        #choose where disk is to be pushed or choose another stack to pick up from    
        print("Where do you want to put the disk? [l, m, r, q]")
        to_stack = get_stack("foo")
        if to_stack:
                           
            #validating move
            if not to_stack.is_empty() and from_stack.peek() > to_stack.peek():
                print("You can't put a disk onto a smaller one")
                continue
                
            #move the disk
            else:
                to_stack.push(from_stack.pop())
                n_moves += 1
                break
        break

"""
End game
"""
print_screen()
print("Congratulation, you beated the game!")
print("You made {} moves.".format(n_moves))
if n_moves == n_optimal_moves:
    print("Amazing, you finished the game as fast as possible!")
input("Press any key to exit this program. See you soon!")
