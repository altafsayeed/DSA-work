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

    def __r_contains(self, current_node, value):
        if current_node == None:                                    # This condition is met when a value doesn't exist
            return False
        if value == current_node.value:                             # When a value is found
            return True
        if value < current_node.value:                              # If value is less than current node, call function again with node to left
            return self.__r_contains(current_node.left, value)
        if value > current_node.value:                              # If value is greater than current node, call function again with node to right
            return self.__r_contains(current_node.right, value)
                
    def r_contains(self, value):
        return self.__r_contains(self.root, value)


my_tree = BinarySearchTree()
my_tree.insert(47)
my_tree.insert(21)
my_tree.insert(76)
my_tree.insert(18)
my_tree.insert(27)
my_tree.insert(52)
my_tree.insert(82)

print('BST Contains 27:')
print(my_tree.r_contains(27))

print('\nBST Contains 17:')
print(my_tree.r_contains(17))