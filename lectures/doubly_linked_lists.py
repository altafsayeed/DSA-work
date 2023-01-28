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


my_doubly_linked_list = DoublyLinkedList(7)
my_doubly_linked_list.append(10)

print(my_doubly_linked_list.pop())
print(my_doubly_linked_list.pop())
print(my_doubly_linked_list.pop())