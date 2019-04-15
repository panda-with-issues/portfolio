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
    
    #add child to a node 
    def add_child(self, data):
        new_node = __init__(data)
        self.children


class Tree:
    
    #allow to declare a root node while instantiating the tree
    def __init__(self, root=None):
        if root:
            self.root = TreeNode(root)
            self.root.level = 0
        else:
            self.root = root

    def __str__(self):
        return "A tree with root {}".format(self.root.data)

    #set tree's root node. If passed argument is not a TreeNode object, instantiate it
    def set_root(self, root):
        if type(root) != TreeNode:
            root = TreeNode(root)
        self.root = root
        self.root.level = 0
