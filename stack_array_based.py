class Stack(object):
    def __init__(self, *vals):
        for val in vals:
            push(val)

    def push(val):
        self._vals.append(val)
        return True

    def pop():
        return self._vals.pop()

    def peek():
        return self._vals[-1]

    def size():
        return len(self._vals)


def test():
    stack = Stack(1,2,3)
    assert stack.size() == 3
    assert stack.pop() == 3

    assert stack.size() == 2
    assert stack.pop() == 2

    assert stack.size() == 1
    assert stack.pop() == 1

    assert stack.size() == 0
    assert stack.push(10) == True
    assert stack.size() == 1

    assert stack.peek() == 10
    assert stack.push(20) == True
    assert stack.peek() == 20
    assert stack.size() == 2
