# -*- coding: utf-8 -*-

class Node():
    def __init__(self):
        self.data = None
        self.next = None


    def setItem(self, item):
        self.data = item


    def getItem(self):
        return self.data

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
