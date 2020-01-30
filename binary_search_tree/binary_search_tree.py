import sys
sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack

"""
Binary Search Tree
        x
    x       x
x       x       x
"""

## BinarySearchTree(somevalue) creates a node at the ROOT of the BST equal to somevalue; establishing a ROOT node.
class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if value == self.value:
            return f"{value} is already in the tree"
        elif value < self.value:
            if self.left:
                self.left.insert(value)
            else:
                self.left = BinarySearchTree(value)
        else:
            if self.right:
                self.right.insert(value)
            else:
                self.right = BinarySearchTree(value)


    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value == target:
            return True
        elif target < self.value:
            if self.left:
                return self.left.contains(target)
        else:
            if self.right:
                return self.right.contains(target)
        return False 

    # Return the maximum value found in the tree
    def get_max(self):
        if self.right:
            return self.right.get_max()
        return self.value

    # def get_max2(self):
    #     if self.right:
    #         return self.right.value
    #     return self.value

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        # implementing on root
        cb(self.value)
        if self.left:
            self.left.for_each(cb)
        if self.right: 
            self.right.for_each(cb)


    # DAY 2 Project -----------------------
    """
    insertion order: 8, 5, 7, 6, 3, 4, 2
                8
            5
        3           7
    2       4   6
    """

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node=None):
        if self.left:
            self.left.in_order_print()
        print(self.value)
        if self.right:
            self.right.in_order_print()

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        q=Queue() 
        q.enqueue(node) 
        while q.len() > 0:
            current = q.dequeue() 
            print(current.value)
            if current.left:
                q.enqueue(current.left)
            if current.right:
                q.enqueue(current.right)
            

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        s = Stack()
        s.push(node)
        while s.len() > 0:
            current = s.pop()
            print(current.value)
            if current.left:
                s.push(current.left)
            if current.right:
                s.push(current.right)


    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print In-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass


# bst = BinarySearchTree(90)
# bst.insert(8)
# print(bst.in_order_print(bst))
# bst.insert(102)
# bst.insert(102)
# bst.insert(88)
# bst.insert(400)

# print(bst.for_each(bst.get_max2()))