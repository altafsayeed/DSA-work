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

    def contains(self, value):
        temp = self.root                # Create temp and point it to the root
        while temp is not None:         # While temp is pointing to a node
            if value < temp.value:      # If value is less than temp, move temp down to the left
                temp = temp.left
            elif value > temp.value:    # If value is greater than temp, move temp down to the right
                temp = temp.right
            else:
                return True             # If value is equal to temp, we have found the node, return True
        return False                    # If we hit None, node not found, while loop gets skipped, return False

my_tree = BinarySearchTree()
my_tree.insert(47)
my_tree.insert(21)
my_tree.insert(76)
my_tree.insert(18)
my_tree.insert(27)
my_tree.insert(52)
my_tree.insert(82)

print(my_tree.contains(27))

print(my_tree.contains(17))