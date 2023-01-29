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
    
    def insert(self, index, value):
        if index < 0 or index > self.length:       # If index is out of range, return False
            return False
        if index == 0:                          # If index is equal to the head, use prepend
            return self.prepend(value)
        if index == self.length:                # If index is equal to tail, use append
            return self.append(value)
        new_node = Node(value)                  
        before = self.get(index - 1)            # Create before variable and point to node before the insert index
        after = before.next                     # Create after variable and point to node after the insert index
        new_node.prev = before                  # Set new node's prev node to before node
        new_node.next = after                   # Set new node's next node to after node
        before.next = new_node                  # Set before's next node to new node
        after.prev = new_node                   # Set after's prev node to new node
        self.length += 1
        return True
    
    def remove(self, index):
        if index < 0 or index >= self.length:       
            return None
        if index == 0:                      # If index equals head, use pop_first 
            return self.pop_first()         
        if index == self.length - 1:        # If index equals tail, use pop
            return self.pop()
        temp = self.get(index)              
        before = temp.prev              # Create before variable and assign to temp's previous node
        after = temp.next               # Create after variable and assign to temp's next node
        temp.next = None                # Cut connection to next node
        temp.prev = None                # Cut connection to previous node
        before.next = after             # Set before's next node to node after the one we're removing
        after.prev = before             # Set after's previous node to node before the one we're removing
        self.length -= 1
        return temp
    
    def remove2(self, index):                   # Same function, but without using before and after variables. Only using temp
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
        temp = self.get(index)
        temp.next.prev = temp.prev
        temp.prev.next = temp.next
        temp.next = None
        temp.prev = None
        self.length -= 1
        return temp




my_doubly_linked_list = DoublyLinkedList(11)
my_doubly_linked_list.append(3)
my_doubly_linked_list.append(23)
my_doubly_linked_list.append(7)

my_doubly_linked_list.print_list()

my_doubly_linked_list.remove(2)

print("After remove:")
my_doubly_linked_list.print_list()