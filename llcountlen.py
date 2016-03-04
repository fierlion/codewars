class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

def length(node):
    list_length = 0
    while node.next is not None:
        node = node.next
        list_length += 1

def count(node, data):
    hits = 0
    while node.next is not None:
        if node.value == data:
            hits += 1
        node = node.next
    
