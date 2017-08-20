# -*- coding: utf-8 -*-

"""
How to create a fixed list:

    https://stackoverflow.com/questions/5944708/python-forcing-a-list-to-a-fixed-size

Deep Copy VS Shallow Copy:

    Two problems often exist with deep copy operations that don’t exist with shallow copy operations:
    1. Recursive objects (compound objects that, directly or indirectly, contain a reference to themselves) may cause a recursive loop.

    2. Because deep copy copies everything it may copy too much, such as data which is intended to be shared between copies.

    dict.copy() and list1[:] are shallow copies.
"""


from collections import deque


class FixCapacityStack1():
    def __init__(self, size):
        """Create a fixed size list using deque()

        deque doesn't support slice.
        """
        self.data = deque(maxlen=size)
        self.size = size


    def isEmpty(self):
        return not len(self.data)


    def getSize(self):
        return len(self.data)


    def push(self, item):
        self.data.append(item)


    def pop(self):
        if not self.isEmptry():
            return self.data.pop()
        else:
            return None


class FixCapacityStack2():
    def __init__(self, size):
        self.size = size
        self.data = []


    def isEmpty(self):
        return not len(self.data)


    def getSize(self):
        return len(self.data)


    def push(self, item):
        self.data.append(item)
        if len(self.data) > self.size:
            self.data[:1] = []


    def pop(self):
        if not self.isEmptry():
            return self.data.pop(-1)


class ResizingStack():
    def __init__(self):
        self.size = 8
        self.data = deque(maxlen=self.size)


    def isEmpty(self):
        return not len(self.data)


    def getSize(self):
        return len(self.data)


    def resize(self, new_size):
        self.size = new_size
        self.data = deque([_ for _ in self.data], maxlen=self.size)


    def push(self, item):
        self.data.append(item)
        len(self.data) < self.size or self.resize(2*self.size)


    def pop(self):
        ret = None
        if not self.isEmpty():
            ret = self.data.pop()
            if len(self.data) and len(self.data) < self.size/4:
                self.resize(int(self.size/2)) # self.size/2 returns a float.

        return ret



if __name__ == '__main__':
    # stack = FixCapacityStack2(100)
    stack = ResizingStack()
    tobe = ('to', 'be', 'or', 'not', 'to', '-', 'be', '-', '-', 'that', '-', '-', '-', 'is')

    for t in tobe:
        if t == '-':
            stack.isEmpty() or print(stack.pop())
        else:
            stack.push(t)

    print('({0} left on stack.)'.format(stack.getSize()))
