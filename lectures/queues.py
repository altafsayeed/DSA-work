class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self, value):
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.length = 1

    def print_queue(self):
        temp = self.first
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def enqueue(self, value):
        new_node = Node(value)
        if self.first is None:            # If empty queue, set first and last equal to new node
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node   # Set last node's next node to the new node
            self.last = new_node        # Set last node equal to the new node
        self.length += 1

my_queue = Queue(1)
my_queue.enqueue(2)

my_queue.print_queue()