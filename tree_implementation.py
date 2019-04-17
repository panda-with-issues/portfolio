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
        if type(new_node) != TreeNode:
            new_node = TreeNode(new_node)
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

    #traverse the tree to found and return a node, given its data
    def traverse(self, wanted_data):
        nodes_to_be_searched = [self.root]
        while nodes_to_be_searched:
            current_node = nodes_to_be_searched.pop()
            if current_node.data == wanted_data:
                return current_node
            nodes_to_be_searched += current_node.children         

    #add a child to a given node. If child is not a node, instantiate it. Share interface with similar TreeNode's method
    def add_child(self, parent, child):
        if type(child) != TreeNode:
            child = TreeNode(child)
        if type(parent) != TreeNode:
            parent = self.traverse(parent)
        parent.add_child(child)
    
    #remove child given its data. Share interface with similar TreeNode's method
    def remove_child(self, kill_me):
        if type(kill_me) != TreeNode:
            kill_me = self.traverse(kill_me)
        nodes_to_check = [self.root]
        while nodes_to_check:
            current_node = nodes_to_check.pop()
            if kill_me in current_node.children:
                current_node.remove_child(kill_me)
                break
            nodes_to_check += current_node.children

    #print a visual representation of Tree
    def graph(self):
        nodes_to_print = [self.root]
        while nodes_to_print:
            current_node = nodes_to_print.pop()
            if current_node is self.root:
                print(current_node.data)
            else:
                branches = "|"
                if current_node.level > 1:
                    for i in range(1, current_node.level):
                        branches += "   |" 
                print(branches)
                print(branches + "---" + str(current_node.data))
            nodes_to_print += current_node.children


class BranchOverflow(Exception):
    "BranchOverflow Error: this node can't have more than two children"

#in this subclass, every node can have at most two children
class BinaryTreeNode(TreeNode):

    #update constructor to hold a hashed value that will be used in node's comparisons
    def __init__(self, data):
        super().__init__(data)
        if type(data) == str:
            self.value = sum(data.encode())
        elif type(data) == list or type(data) == dict or type(data) == tuple:
            self.value = len(data)
        elif type(data) == float:
            self.value = round(float)
        else:
            self.value = data

    def __str__(self):
        return "A binary node with data {}".format(self.data)

    #update method to check whether the node has less than two children and to always have the smaller child at index 0
    def add_child(self, child):
        if len(self.children) < 2:
            if type(child) != BinaryTreeNode:
                child = BinaryTreeNode(child)
            self.children.append(child)
            child.level = self.level + 1
            #check order
            if len(self.children) == 2:
                first = self.children[0]
                second = self.children[1]
                if first.value > second.value:
                    self.children.reverse()
        else:
            raise BranchOverflow

class BinaryTree(Tree):

    def __init__(self, root=None):
        if root:
            self.root = BinaryTreeNode(root)
            self.root.level = 0
        else:
            self.root = root


    def __str__(self):
        return "A binary tree with root {}".format(self.root)

    #overwrite add_child method. New node's position is enstablished by node's value
    def add_child(self, child):
        if type(child) != BinaryTreeNode:
            child = BinaryTreeNode(child)

        current_node = self.root
        while current_node:

            #if current node has no child, add child and exit the loop
            if len(current_node.children) == 0:
                current_node.add_child(child)
                break

            #if current node already has a child, two case must be dinguished: if child is a right node or a left node
            elif len(current_node.children) == 1:
                
                #if child is a left node (minor than parent), a child can be added only if its value is greater than parent's
                if current_node.value > current_node.children[0].value and child.value >= current_node.value:
                    current_node.add_child(child)
                    break
                #if child is a right node (greater than or equal to parent), a child can be added only if its value is minor than parent's
                elif current_node.value <= current_node.children[0].value and child.value < current_node.value:
                    current_node.add_child(child)
                    break
                #otherwise move to existing child
                else:
                    current_node = current_node.children[0]
            
            #if current node alrady has two child, move to left node if child's value is minor than parent's; else move right
            elif child.value < current_node.value:
                current_node = current_node.children[0]
            else:
                current_node = current_node.children[1]
                    
        
import random
tree = BinaryTree(50)
nodini = [random.randint(0, 100) for n in range(10)]
print(nodini)
for cosa in nodini:
    tree.add_child(cosa)
tree.graph()