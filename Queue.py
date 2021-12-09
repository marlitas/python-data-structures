class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self, value):
        new_node = Node(value)
        #head is first
        self.first = new_node
        #tail is last
        self.last = new_node
        self.length = 1

    def print_queue(self):
        node = self.first
        while node is not None:
            print(node.value)
            node = node.next

    def enqueue(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.length += 1
        return True

    def dequeue(self):
        if self.length == 0:
            return None
        old_node = self.first
        if self.length == 1:
            self.first = None
            self.last = None
        else:
            self.first = old_node.next
            old_node.next = None
        self.length -= 1
        return old_node


my_queue = Queue(1)
my_queue.enqueue(2)

print(my_queue.dequeue())
print(my_queue.dequeue())
print(my_queue.dequeue())

my_queue.print_queue()