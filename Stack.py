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
        if self.top is None:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.height += 1
        return True

    def pop(self):
        if self.top is None:
            return None
        old_node = self.top
        self.top = old_node.next
        old_node.next = None
        self.height -= 1
        return old_node
        



my_stack = Stack(4)
my_stack.push(3)

print(my_stack.pop())
print(my_stack.pop())
print(my_stack.pop())

my_stack.print_stack()