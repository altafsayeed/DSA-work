class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__ (self):
        self.root = None        # This is the top of the tree

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:           # If empty tree, make the new node the root
            self.root = new_node
            return True
        temp = self.root                # Create temp variable and point it to the root
        while(True):
            if new_node.value == temp.value:  # Stop the loop if the new node and temp's values are equal
                return False
            if new_node.value < temp.value:     # If new node is less than temp, go to the left side
                if temp.left is None:           # If there is no node here, insert new node
                    temp.left = new_node
                    return True
                temp = temp.left                # Move temp to the next node
            else:
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right

my_tree = BinarySearchTree()
my_tree.insert(2)
my_tree.insert(1)
my_tree.insert(3)

print(my_tree.root.value)
print(my_tree.root.left.value)
print(my_tree.root.right.value)