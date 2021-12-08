class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
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
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True
        
    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True  

    def pop(self):
        if self.length == 0:
            return None
        temp = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = temp.prev
            self.tail.next = None
            temp.prev = None
        self.length -= 1
        return temp

    def pop_first(self):
        if self.length == 0:
            return None
        node = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = node.next
            self.head.prev = None
            node.next = None
        self.length -= 1
        return node.value

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        node = self.head
        if index < self.length/2:
            for _ in range(index):
                node = node.next
        else:
            node = self.tail
            for _ in range(self.length - 1, index, -1):
                node = node.prev
        return node
    
    def set_value(self, index, value):
        node = self.get(index)
        if node:
            node.value = value
            return True
        return False

    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        new_node = Node(value)
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        before = self.get(index-1)
        after = before.next
        before.next = new_node
        after.prev = new_node
        new_node.prev = before
        new_node.next = after
        self.length += 1
        return True
    
    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
        before = self.get(index - 1)
        node = before.next
        after = node.next
        before.next = after
        after.prev = before
        node.prev = None
        node.next = None
        self.length -= 1
        return node
        
my_doubly = DoublyLinkedList(0)
my_doubly.append(1)
my_doubly.append(2)
my_doubly.remove(1)
my_doubly.print_list()