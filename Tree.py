# A full tree either points to two nodes or no nodes
# A perfect tree (also full) points to no nodes
# A complete tree is filled in from left to right. 

# A parent has two child nodes
# If nodes come from the same parent, they are siblings. 
# Nodes can only come from one parent. 
# If a node has no children, it is called a leaf. 


#Binary search tree
    # if a node is greater than the parent goes to the right. If its less than the parent. Goes to the left. 
    # If the parent right spot is already taken compare to the node there, and continue.
    # Any node in the binary search tree will have values less than on the left, and greater than on the right. 

# Treat it as O(log n), but technically worst case scenario is that its a linked list and is O(n)
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True
        temp = self.root
        while (True):
            if new_node.value == temp.value:
                return False
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right
                
    def contains(self, value):
        temp = self.root
        while temp is not None:
            if value == temp.value:
                return True
            if value < temp.value:
                temp = temp.left
            else:
                temp = temp.right
        return False

    def min_value_node(self, current_node):
        while current_node.left is not None:
            current_node = current_node.left
        return current_node


my_tree = BinarySearchTree()
my_tree.insert(5)
my_tree.insert(1)
my_tree.insert(2)
my_tree.insert(8)
my_tree.insert(7)

print(my_tree.min_value_node(my_tree.root))
print(my_tree.min_value_node(my_tree.root.right))