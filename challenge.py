"""
m  x  x  x  x  x  x  x  x  x  x  x  x
m  c  x  x  x  x  x  x  x  x  x  x  x
x  m  c  x  x  x  x  x  x  x  x  x  x
x  m  x  c  x  x  x  x  x  x  x  x  x
x  x  m  x  c  x  x  x  x  x  x  x  x
x  x  m  x  x  c  x  x  x  x  x  x  x
x  x  x  m  x  x  c  x  x  x  x  x  x
x  x  x  m  x  x  x  c  x  x  x  x  x
"""

class SLNode:
    def __init__(self, value):
        self.value = value
        self.next = None

class SL_List:
    def __init__(self, node=None):
        self.head = node

    def add_to_head(self, value):
        new_node = SLNode(value)
        if not self.head:
            self.head = new_node
        else: 
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node


def find_middle_node(list):
    counter = 0
    middle = list.head
    current = list.head

    while current.next:
        counter +=1
        current = current.next
        if counter % 2 is 0:
            middle = middle.next
    return middle

test = SLNode('test')
list = SL_List(test)


'''
temp, 
current

h a b c d e f g h i j k l m
c n   
a h b c d e f g h i j k l m
  c n
a h b c d e f g h i j k l m
'''


