class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__ (self):
        self.root = None        # This is the top of the tree

my_tree = BinarySearchTree()

print(my_tree.root)