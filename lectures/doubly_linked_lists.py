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
            self.tail.next.prev = self.tail     # Set tail's next node's previous node to old tail
            self.tail = new_node                # Finally, assign tail to the new node

my_doubly_linked_list = DoublyLinkedList(7)
my_doubly_linked_list.append(10)
my_doubly_linked_list.append(1)
my_doubly_linked_list.append(17)

my_doubly_linked_list.print_list()