"""
Choose you own adventure: Wilderness Escape
An excersise with tree data structure
"""

from tree_implementation import Tree as Tre, TreeNode

class Tree(Tre):
    def teller(self):
        story_node = self.root
        print(story_node.data)
        while story_node.children:
            valid_input = [1,2]
            choice = int(input("Enter 1 or 2 to continue the story: "))
            while choice not in valid_input:
                choice = int(input("Invalid input. Enter 1 or 2 to continue the story: "))
            chosen_child = story_node.children[choice - 1]
            print(chosen_child.data)
            story_node = chosen_child
        

beginning = """You are in a forest clearing. There is a path to the left.
A bear emerges from the trees and roars!
Do you: 
1 ) Roar back!
2 ) Run to the left..."""
story = Tree(beginning)

choice_a = TreeNode(#
"""
The bear is startled and runs away.
Do you:
1 ) Shout 'Sorry bear!'
2 ) Yell 'Hooray!'
""")

choice_b = TreeNode(#
"""
You come across a clearing full of flowers. 
The bear follows you and asks 'what gives?'
Do you:
1 ) Gasp 'A talking bear!'
2 ) Explain that the bear scared you.
""")

story.root.add_child(choice_a)
story.root.add_child(choice_b)

choice_a_1 = TreeNode(#
"""
The bear returns and tells you it's been a rough week. After making peace with
a talking bear, he shows you the way out of the forest.

YOU HAVE ESCAPED THE WILDERNESS.
""")
choice_a_2 =(#
"""
The bear returns and tells you that bullying is not okay before leaving you alone
in the wilderness.

YOU REMAIN LOST.
""")

choice_a.add_child(choice_a_1)
choice_a.add_child(choice_a_2)

choice_b_1 = (
    """
The bear is unamused. After smelling the flowers, it turns around and leaves you alone.

YOU REMAIN LOST.
"""
)
choice_b_2 = (
    """
The bear understands and apologizes for startling you. Your new friend shows you a 
path leading out of the forest.

YOU HAVE ESCAPED THE WILDERNESS.
"""
)

choice_b.add_child(choice_b_1)
choice_b.add_child(choice_b_2)

story.teller()