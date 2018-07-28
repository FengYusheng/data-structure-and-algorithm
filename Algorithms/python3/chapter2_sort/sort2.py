# -*- coding: utf-8 -*-

import sys
import random
from collections import deque

def selection_sort(data=[]):
    length = len(data)

    for i in range(length):
        min = data[i]

        for j in range(i, length):
            if min > data[j]:
                min, data[j] = data[j], min

    return data


def insertion_sort(data=[]):
    length = len(data)

    for i in range(length-1):
        j = i + 1

        while j > 0:
            if data[j] < data[j-1]:
                data[j-1], data[j] = data[j], data[j-1]
                j -= 1
            else:
                break

    return data


def shell_sort(data=[]):
    length = len(data)
    h = 1

    while h < length/3:
        h = 3 * h + 1

    while h >= 1:
        for i in range(h, length):
            while i - h >= 0:
                if data[i] < data[i-h]:
                    data[i], data[i-h] = data[i-h], data[i]
                    i = i - h
                else:
                    break

        h = int(h/3)

    return data



def merge(data, lo, mid, hi):
    i = lo
    j = mid + 1
    pivot = lo
    aux = [i for i in data]

    while pivot <= hi:
        if i > mid:
            data[pivot] = aux[j]
            j += 1
        elif j > hi:
            data[pivot] = aux[i]
            i += 1
        elif aux[j] < aux[i]:
            data[pivot] = aux[j]
            j += 1
        else:
            data[pivot] = aux[i]
            i += 1

        pivot += 1



def merge_sort_top_to_bottom(data = []):
    lo = 0
    hi = len(data) - 1
    mid = int(len(data)/2) if len(data)%2 else int(len(data)/2)-1
    sorted_data = [i for i in data]

    if hi > lo:
        t1 = merge_sort_top_to_bottom(data[lo:mid+1]) # A list slice generates a new list.
        t2 = merge_sort_top_to_bottom(data[mid+1:])
        sorted_data = t1 + t2
        merge(sorted_data, lo, mid, hi)

    return sorted_data


def merge_sort_bottom_to_top(data = []):
    # error
    sorted_data = [i for i in data]
    length = len(data)
    mid = int(length/2) if length%2 else int(length/2)-1

    for interval in range(1, mid)[::2]:
        j = 0
        while True:
            lo = j
            hi = j+interval if j+interval <= length else length-1
            _mid = lo + int((hi-lo)/2)

            merge(sorted_data, lo, _mid, hi)
            print(lo, _mid, hi)

            print(sorted_data)
            if hi == length-1:
                break

            j = hi + 1

    merge(sorted_data, 0, mid, length-1)
    return sorted_data



def merge_sort_bottom_to_top2(data = []):
    length = len(data)
    sorted_data = [i for i in data]
    interval = 1

    while interval < length:
        lo = 0

        while lo < length-interval:
            mid = lo + interval - 1
            hi = min([lo+interval+interval-1, length-1])
            merge(sorted_data, lo, mid, hi)
            lo =  lo + interval * 2

        interval *= 2

    return sorted_data


def partition(data, lo, hi):
    i, j = lo+1, hi

    while True:
        while i < hi and data[i] <= data[lo]:
            i += 1

        while j > lo and data[j] >= data[lo]:
            j -= 1

        if i >= j:
            break

        data[i], data[j] = data[j], data[i]

    data[lo], data[j] = data[j], data[lo]

    return j


def quick_sort(data, lo, hi):
    if lo < hi:
        pivot = partition(data, lo, hi)
        quick_sort(data, lo, pivot-1)
        quick_sort(data, pivot+1, hi)


class MaxPQ:
    def __init__(self, size=None):
        self.pivot = 0
        self.size = size
        self.queue = deque(maxlen=size+1) if size is not None else deque()
        self.queue.append('-')


    def __len__(self):
        return self.size+1 if self.size is not None else sys.maxsize


    def _swim(self):
        n = self.count()
        parent = int(n/2)

        while parent > 0:
            if self.queue[parent] < self.queue[n]:
                self.queue[parent], self.queue[n] = self.queue[n], self.queue[parent]
                n, parent = parent, int(parent/2)
            else:
                break


    def _sink(self):
        n = self.count()
        pivot = 1

        while 2*pivot <= n:
            child_index = 2*pivot+1 if 2*pivot+1 <= n and self.queue[2*pivot+1] > self.queue[2*pivot] else 2*pivot
            if self.queue[pivot] < self.queue[child_index]:
                self.queue[pivot], self.queue[child_index] = self.queue[child_index], self.queue[pivot]
                pivot = child_index
            else:
                break


    def isEmpty(self):
        return len(self.queue) == 1


    def count(self):
        return len(self.queue) - 1


    def insert(self, v):
        self.queue.append(v)
        self._swim()


    def delMax(self):
        m = None
        n = self.count()

        if self.count() > 0:
            m = self.queue[1]
            self.queue[1], self.queue[n] = self.queue[n], self.queue[1]
            self.queue.pop()
            self._sink()

        return m


    def printPQ(self):
        print(self.queue)


class Multiway:
    """
    Priority queue can be used to merge multi streams into an sorted stream.
    """
    def __init__(self, streams=[]):
        self.streams = streams


def heap_sort(data = []):
    def _sink(index):
        pivot = index
        while 2*pivot <= N:
            child_index = 2*pivot+1 if 2*pivot+1<=N and pq[2*pivot+1] > pq[2*pivot] else 2*pivot
            if pq[pivot] < pq[child_index]:
                pq[pivot], pq[child_index] = pq[child_index], pq[pivot]
                pivot = child_index
            else:
                break

    def _build_heap():
        pivot = int(N/2)
        while pivot > 0:
            _sink(pivot)
            pivot -= 1

    N = len(data)
    pq = deque(['-']+data)

    _build_heap()

    while N > 1:
        pq[N], pq[1] = pq[1], pq[N]
        N -= 1
        _sink(1)

    pq.popleft()
    return pq



__all__ = [
    'selection_sort',
    'insertion_sort',
    'shell_sort',
    'merge',
    'merge_sort_top_to_bottom',
    'merge_sort_bottom_to_top',
    'merge_sort_bottom_to_top2',
    'quick_sort',
    'partition',
    'MaxPQ',
    'heap_sort'
]
