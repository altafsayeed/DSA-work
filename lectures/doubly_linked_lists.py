class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None        # The one difference between single and doubly linked list nodes

class DoublyLinkedList:
    def __init__(self, value):      # This is the same as singly linked lists
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
        new_node = Node(value)
        if self.length is None:         # If empty list, point head and tail to new node
            self.head = new_node
            self.tail = new_node
        else:                               
            self.tail.next = new_node           # Set tail's next node to new node
            new_node.prev = self.tail                # Set new node's previous node to old tail
            self.tail = new_node                # Finally, assign tail to the new node
        self.length += 1
        return True
    
    def pop(self):
        if self.length == 0:     # If empty list, return None
            return None
        temp = self.tail         # Create temp variable and assign to tail
        if self.length == 1:    # If only one node in list, set head and tail to None since list will become empty
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev  # Set new tail equal to tail's previous node
            self.tail.next = None       # Set new tail's next node to None to cut connection to last node
            temp.prev = None            # Set temp's (old tail) previous node to None to cut connection
        self.length -= 1
        return temp
    
    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:             # Edge case: If list is empty, set head and tail to new node
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head   # Set new node's next to point to current head
            self.head.prev = new_node   # Set head's previous node to point to new node
            self.head = new_node        # Make new node the new head
        self.length += 1
        return True
    
    def pop_first (self):
        if self.length == 0:
            return None
        temp = self.head            # Create temp to point to node we will pop
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next       # Set head equal to the node after current head
            temp.next = None                # Cut connection from temp to next node
            self.head.prev = None           # Cut connection from second node to first node
        self.length -= 1
        return temp
    
    def get(self, index):
        if index < 0 or index >= self.length:       # If index is out of range, return None
            return None
        temp = self.head                        # Create temp and point at head
        if index < self.length/2:               # If index is in the first half, iterate from the head forward
            for _ in range (index):
                temp = temp.next
        else:                               # If index is in the second half, iterate from the tail backwards
            temp = self.tail
            for _ in range (self.length - 1, index, -1):        # Start at the tail, end at the index, decrement by 1
                temp = temp.prev
        return temp
    
    def set_value (self, index, value):
        temp = self.get(index)          # We can use the get method we made, set temp equal to the node at the index
        if temp:                        # If the index was valid, we will have a temp, otherwise there will be no temp
            temp.value = value          # Set temp node's value to the value passed in
            return True
        return False



my_doubly_linked_list = DoublyLinkedList(11)
my_doubly_linked_list.append(3)
my_doubly_linked_list.append(23)
my_doubly_linked_list.append(7)

my_doubly_linked_list.set_value(1, 69)

my_doubly_linked_list.print_list()
