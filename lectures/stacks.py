class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self, value):
        new_node = Node(value)
        self.top = new_node
        self.height = 1

    def print_stack(self):
        temp = self.top
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def push(self, value):
        new_node = Node(value)
        if self.height == 0:                # If stack is empty, set top to new node
            self.top = new_node
        else:
            new_node.next = self.top        # Set new node's next pointer to the current top
            self.top = new_node             # Set top to the new node
        self.height += 1

    def pop(self):
        if self.height == 0:
            return None
        temp = self.top                 # Create temp variable and set to top
        self.top = self.top.next        # Set top equal to next node
        temp.next = None                # Cut connection from old top to second node
        self.height -= 1
        return temp

my_stack = Stack(2)
my_stack.push(11)
my_stack.push(13)
my_stack.push(14)

my_stack.print_stack()

my_stack.pop()

print("after pop")

my_stack.print_stack()