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
        return "This is the {position} stack with {size} disk(s)".format(position=self.position, size=self.size)

"""
setting up the game
"""

left_stack = Hanoi_stack("left")
middle_stack = Hanoi_stack("middle")
right_stack = Hanoi_stack("right")

stacks = []
stacks.append(left_stack).append(middle_stack).append(right_stack) #correggimi

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
for i in range(5, 1, -1):
    left_stack.push(i)

#prompting the optimal number of moves to solve the game
n_optimal_moves = 2 ** disks - 1
print("The fastest way you can solve this game is in {} moves".format(n_optimal_moves))

#ask user which stack they want to choose
def get_input():
    valid_input = [stack.position[0] for stack in stacks]
    while True:
        input = input(" ").lower().strip()
        if input in valid_input:
            for stack in stacks:
                if input == stack.position[0]:
                    return stack
        else:
            for stack in stacks:
                print("Enter {letter} for {position} stack".format(letter=stack.position[0], position=stack.position))
                continue
