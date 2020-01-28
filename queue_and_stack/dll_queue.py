import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList
from doubly_linked_list import ListNode


test = ListNode('testing')

class Queue:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
            # we can easily access head, tail, next and prev nodes
        self.storage = DoublyLinkedList()

    def enqueue(self, value):
        self.storage.add_to_head(value)
        # increment size
        self.size += 1
        

    def dequeue(self):
        if self.size > 0:
            return self.storage.remove_from_tail()
            self.size -= 1
        else: 
            return None

    def len(self):
        return self.size

