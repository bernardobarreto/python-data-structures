class Queue(object):
    def __init__(self, *vals):
        self._vals = []
        for val in vals:
            self.push(val)

    def push(self, val):
        self._vals.insert(0, val)
        return True

    def pop(self):
        return self._vals.pop()

    def peek(self):
        return self._vals[-1]

    def size(self):
        return len(self._vals)


def test():
    queue = Queue(1,2,3)
    assert queue.size() == 3
    assert queue.pop() == 1

    assert queue.size() == 2
    assert queue.pop() == 2

    assert queue.size() == 1
    assert queue.pop() == 3

    assert queue.size() == 0
    assert queue.push(10) == True
    assert queue.size() == 1

    assert queue.peek() == 10
    assert queue.push(20) == True
    assert queue.peek() == 10
    assert queue.size() == 2

if __name__ == '__main__':
    test()
