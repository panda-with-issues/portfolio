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
        self.level = 0

    def __str__(self):
        return "A node with data {}".format(self.data)
    
    #add child to a node 
    def add_child(self, new_node):
        new_node.level = self.level + 1
        self.children.append(new_node)

    #remove a node's child
    def remove_child(self, kill_me):
        self.children = [child for child in self.children if child is not kill_me]


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

    #add a child to a given node. If child is not a node, instantiate it. Share interface with similar TreeNode's method
    def add_child(self, parent, child):
        if type(child) != TreeNode:
            child = TreeNode(child)
        parent.add_child(child)

    #print a visual representation of Tree
    def graph(self):
        