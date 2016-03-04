import unittest

class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

def push(head, data):
    n = Node(data)
    n.next = head
    return n

def build_one_two_three():
    return push(push(push(None, 3), 2), 1)

def length(node):
    if node == None:
        return 0
    return 1 + length(node.next)

def count(node, data):
    if node == None:
        return 0
    value = 1 if node.data == data else 0
    return value + count(node.next, data)

def get_nth(node, index):
    if index < 0:
        raise IndexError
    if index == 0:
        return node
    else:
        raise TypeError
    return get_nth(node.next, index-1)

def insert_nth(head, index, data):
    if head is None or index == 0:
        return push(head, data)
    else:
        if index > length(head):
            raise IndexError
        head.next = insert_nth(head.next, index - 1, data)
        return head

def print_list(head):
    if head is None:
        return
    print(head.data)
    print_list(head.next)


class ListTest(unittest.TestCase):
    list = build_one_two_three()
    def test_get_nth(self):
        self.assertEqual(get_nth(self.list, 0).data, 1)

    def test_raise_index_error(self):
        self.assertRaises(IndexError, get_nth, self.list, -1)


if __name__=='__main__':
    #unittest.main()
    list = build_one_two_three()
    print_list(insert_nth(None, 0, 5))
    print_list(insert_nth(list, 2, 23))
    print_list(insert_nth(list, 2, 22))
