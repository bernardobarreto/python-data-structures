class Item(object):
    def __init__(self, value='', priority=0):
        self.value = value
        self.priority = priority

class MaxPriorityQueue(object):
    def __init__(self):
        self._data = []
    
    def enqueue(self, item):
        self._data.append(item)
        return True

    def dequeue(self):
        return self._data.pop(self._data.index(self.peek()))

    def peek(self):
        return max(self._data, key=lambda item: item.priority)

    @property
    def size(self):
        return len(self._data)


def test():
    item1 = Item(value='A', priority=10)
    item2 = Item(value='B', priority=1)
    item3 = Item(value='C', priority=5)

    queue = MaxPriorityQueue()

    # size
    assert queue.size == 0

    # enqueue
    assert queue.enqueue(item1) == True
    assert queue.enqueue(item2) == True
    assert queue.enqueue(item3) == True
    assert queue.size == 3

    # peek
    assert queue.peek().value == item1.value

    # dequeue
    assert queue.dequeue().value == item1.value
    assert queue.size == 2
    assert queue.dequeue().value == item3.value
    assert queue.size == 1
    assert queue.dequeue().value == item2.value
    assert queue.size == 0

if __name__ == '__main__':
    test()