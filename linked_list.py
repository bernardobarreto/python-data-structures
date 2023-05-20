class LinkedList(object):
    def __init__(self, arg, *args):
        self.head = Node(arg)
        last_node = self.head
        for val in args:
            last_node.next = Node(val)
            last_node = last_node.next


class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None


def test():
    head = LinkedList(1, 2, 3).head
    assert head.val == 1
    node1 = head.next
    assert node1.val == 2
    node2 = node1.next
    assert node2.val == 3

if __name__ == '__main__':
    test();
