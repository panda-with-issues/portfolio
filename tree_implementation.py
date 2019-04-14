"""
Complex Data Structure
Tree implementation in Python3
"""

class TreeNode:

    def __init__(self, data):
        self.data = data
        #here every current node's child node is listed
        self.children = []
        #distance from root node
        self.level = None
    
    def add_children(self, node):

class Tree:
    
    #allow to declare a root node while instantiating the tree
    def __init__(self, root=None):
        if root:
            self.root = TreeNode(root)
            self.root.level = 0
        else:
            self.root = root