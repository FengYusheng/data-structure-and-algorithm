# -*- coding: utf-8 -*-

class Node():
    def __init__(self):
        self.data = None
        self.next = None


    def setItem(self, item):
        self.data = item


    def getItem(self):
        return self.data


    def setNext(self, node):
        self.next = node


    def getNext(self):
        return self.next


class Stack():
    def __init__(self):
        self.first = None
        self.last = None
        self.N = 0


    def isEmpty(self):
        return self.first is None
        # return self.N == 0


    def getSize(self):
        return self.N


    def push(self, item):
        old_first = self.first
        new_node = Node()
        new_node.setItem(item)
        self.N += 1
        new_node.setNext(old_first)
        self.first = new_node


    def pop(self):
        item = None
        if not self.isEmpty():
            item = self.first.getItem()
            self.first = self.first.getNext()
            self.N -= 1

        return item


class Bag():
    """
    iterators & generators: http://anandology.com/python-practice-book/iterators.html

    In python3, you need impelement __next__ method rather than next():

        https://www.python.org/dev/peps/pep-3114/
    """
    def __init__(self):
        self.first = None
        self.N = 0


    def __iter__(self):
        return self


    def isEmpty(self):
        return self.first is None # self.N == 0


    def getSize(self):
        return self.N


    def add(self, item):
        new_node = Node()
        new_node.setItem(item)
        new_node.setNext(self.first)
        self.first = new_node
        self.N += 1


    def __next__(self):
        if not self.isEmpty():
            data = self.first.getItem()
            self.first = self.first.getNext()
            return data
        else:
            raise StopIteration()


class Queue():
    def __init__(self):
        self.first = None
        self.last = None
        self.N = 0


    def isEmpty(self):
        return self.first is None # or self.N == 0


    def getSize(self):
        return self.N


    def enqueue(self, item):
        old_last = self.last
        new_last = Node()
        new_last.setItem(item)
        self.last = new_last
        if not self.isEmpty():
            old_last.setNext(new_last)
        else:
            self.first = new_last

        self.N += 1


    def dequeue(self):
        data = None
        if not self.isEmpty():
            data = self.first.getItem()
            self.first = self.first.getNext()
            self.N -= 1

            if self.isEmpty():
                self.last = self.first

        return data



if __name__ == '__main__':
    # stack = Stack()
    tobe = ('to', 'be', 'or', 'not', 'to', '-', 'be', '-', '-', 'that', '-', '-', '-', 'is')

    for t in tobe:
        if '-' == t:
            print(stack.pop())
        else:
            stack.push(t)

    print('({0} left on stack)'.format(stack.getSize()))

    queue = Queue()

    for t in tobe:
        if '-' == t:
            print(queue.dequeue())
        else:
            queue.enqueue(t)

    print('{0} left on queue'.format(queue.getSize()))

    bag = Bag()
    for t in tobe:
        bag.add(t)

    for _ in bag:
        print(_)
