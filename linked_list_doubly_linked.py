class DoublyLinkedList(object):
    def __init__(self, arg, *args):
        self.head = Node(arg)
        last_node = self.head
        prev_node = None
        for val in args:
            last_node.next = Node(val)
            prev_node = last_node
            last_node = last_node.next
            last_node.prev = prev_node


class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None


def test():
    head = DoublyLinkedList(1, 2, 3).head
    assert head.val == 1
    node1 = head.next
    assert node1.val == 2
    node2 = node1.next
    assert node2.val == 3

    assert node2.prev.val == 2
    assert node2.prev.prev.val == 1

if __name__ == '__main__':
    test();
