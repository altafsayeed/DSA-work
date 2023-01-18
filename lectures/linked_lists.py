class Node:
    def __init__ (self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        new_node = Node(value)  # Create new node variable using Node class
        if self.head is None:   # Edge case: If the linked list is empty
            self.head = new_node    # Set head and tail to the new node since it's the only node
            self.tail = new_node
        else:
            self.tail.next = new_node   # Set tail.next from None to the new node
            self.tail = new_node    # Set tail to point to the new node
        self.length += 1

    def pop(self):
        if self.length == 0: # Edge case 1: If the list is empty
            return None
        temp = self.head    # Assigning temp and pre to the head
        pre = self.head
        while (temp.next):  # While there is a next node
            pre = temp      # Move pre to next node according to previous iteration
            temp = temp.next # Move temp to next node
        self.tail = pre     # Set tail equal to node before the one being removed
        self.tail.next = None # Set tail.next equal to None to remove last node
        self.length -=1 
        if self.length == 0: # Edge case 2: If list only has 1 node
            self.head = None # If after popping node, the length is zero, we need to remove the current head and tail values,
            self.tail = None # since they are still being stored
        return temp # Must return the node being popped to remove it

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:    # Edge case: If list is empty, set head and tail to new node
            self.head = new_node
            self.tail = new_node
        else: 
            new_node.next = self.head   # Set new_node's next value to the current head
            self.head = new_node    # Change current head to new node
        self.length += 1
        return True



linked_list = LinkedList(2)
linked_list.append(3)

linked_list.prepend(1)

linked_list.print_list()