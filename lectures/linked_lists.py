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
        return True

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

    def pop_first(self):
        if self.length == 0: # Edge case 1: If list is empty, return None
            return None
        temp = self.head    # Create temp and point it to the head
        self.head = self.head.next  # Change the head to the next node
        temp.next = None    # Set original head's next to None
        self.length -= 1
        if self.length == 0:    # Edge case 2: If list is empty after decrementing,
            self.tail = None    # Set tail to None since it's still pointing to a node
        return temp

    def get(self, index):
        if index < 0 or index >= self.length:   # Check if index value is valid
            return None
        temp = self.head    # Create temp variable and set it to the head
        for _ in range(index):  # Create for loop from 0 to the index value, loop will stop at the index value
            temp = temp.next    # Go to next node in each iteration
        return temp

    def set_value(self, index, value):
        temp = self.get(index)  # We can use the get method we made, set temp equal to the node at the index
        if temp:    # If the index was valid, we will have a temp, otherwise there will be no temp
            temp.value = value  # Set temp node's value to the value passed in
            return True
        return False
    
    def insert(self, index, value):
        if index < 0 or index > self.length:    # If index is out of range, return false
            return False
        if index == 0:                          # If trying to insert at beginning of list, use prepend
            return self.prepend(value)
        if index == self.length:                # If trying to insert at end of list, use append
            return self.append(value)
        new_node = Node(value)                  # Create new node with value passed in
        temp = self.get(index - 1)              # Create temp variable and let it point to node right before the insert position
        new_node.next = temp.next               # Set new node's next node to the next node of temp
        temp.next = new_node                    # Set temp's next node to be the new node
        self.length += 1
        return True
    
    def remove(self, index):
        if index < 0 or index >= self.length:   # If index is out of bounds, return None
            return None
        if index == 0:                          # If trying to remove node at beginning of list, use pop_first()
            return self.pop_first()
        if index == self.length - 1:            # If trying to remove node at end of list, use pop()
            return self.pop()
        prev = self.get(index - 1)              # Create prev variable and assign to node right before the one we're removing
        temp = prev.next                        # Create temp variable and assign to prev's next node (the one we're removing)
        prev.next = temp.next                   # Assign prev.next to the node after the node we're removing
        temp.next = None                        # Make temp.next equal to None so it cuts off the connection
        self.length -= 1
        return temp



linked_list = LinkedList(11)
linked_list.append(3)
linked_list.append(23)
linked_list.append(7)

print(linked_list.remove(2), '\n')

linked_list.print_list()
