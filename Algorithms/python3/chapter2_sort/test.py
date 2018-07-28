# -*- coding: utf-8 -*-

import sys
import random
import unittest

from sort2 import *

class TestSort(unittest.TestCase):
    def test_selection_sort(self):
        data = ['S', 'O', 'R', 'T', 'E', 'X', 'A', 'M', 'P', 'L', 'E']

        sorted_data = selection_sort(data)
        for i in range(len(sorted_data)-1):
            self.assertLessEqual(sorted_data[i], sorted_data[i+1])


    def test_insertion_sort(self):
        data = ['S', 'O', 'R', 'T', 'E', 'X', 'A', 'M', 'P', 'L', 'E']

        sorted_data = insertion_sort(data)
        for i in range(len(sorted_data)-1):
            self.assertLessEqual(sorted_data[i], sorted_data[i+1])


    def test_shell_sort(self):
        data = ['S', 'O', 'R', 'T', 'E', 'X', 'A', 'M', 'P', 'L', 'E']

        sorted_data = shell_sort(data)
        for i in range(len(sorted_data)-1):
            self.assertLessEqual(sorted_data[i], sorted_data[i+1])


    def test_merge(self):
        data = ['E', 'E', 'G', 'M', 'R', 'A', 'C', 'E', 'R', 'T']
        lo = 0
        hi = len(data) - 1
        mid = int(len(data)/2) if len(data) % 2 else int(len(data)/2) - 1
        # mid = lo + int((hi-lo)/2)
        merge(data, lo, mid, hi)
        for i in range(len(data)-1):
            self.assertLessEqual(data[i], data[i+1])


    def test_merge_2(self):
        data = ['E', 'M', 'R']
        lo = 0
        hi = len(data) - 1
        mid = int(len(data)/2) if len(data) % 2 else int(len(data)/2) - 1
        merge(data, lo, mid, hi)
        for i in range(len(data)-1):
            self.assertLessEqual(data[i], data[i+1])


    def test_merge_sort_top_to_bottom(self):
        data = ['M', 'E', 'R', 'G', 'E', 'S', 'O', 'R', 'T', 'E', 'X', 'A', 'M', 'P', 'L', 'E']
        sorted_data = merge_sort_top_to_bottom(data)
        for i in range(len(sorted_data)-1):
            self.assertLessEqual(sorted_data[i], sorted_data[i+1])


    def test_merge_sort_bottom_to_top(self):
        data = ['M', 'E', 'R', 'G', 'E', 'S', 'O', 'R', 'T', 'E', 'X', 'A', 'M', 'P', 'L', 'E']
        sorted_data = merge_sort_bottom_to_top2(data)
        for i in range(len(sorted_data)-1):
            self.assertLessEqual(sorted_data[i], sorted_data[i+1])


    def test_partition(self):
        data = ['K', 'R', 'A', 'T', 'E', 'L', 'E', 'P', 'U', 'I', 'M', 'Q', 'C', 'X', 'O', 'S']
        self.assertEqual(partition(data, 0, len(data)-1), 5)


    def test_quick_sort(self):
        data = ['Q', 'U', 'I', 'C', 'K', 'S', 'O', 'R', 'T', 'E', 'X', 'A', 'M', 'P', 'L', 'E']
        quick_sort(data, 0, len(data)-1)

        for i in range(len(data)-1):
            self.assertLessEqual(data[i], data[i+1])


    def test_MaxPQ(self):
        self.assertEqual(len(MaxPQ(5)), 6)
        self.assertEqual(len(MaxPQ()), sys.maxsize)
        self.assertTrue(MaxPQ(5).isEmpty())

        pq = MaxPQ()
        data = ['a', 'b', 'c', 'd', 'e']
        random.shuffle(data)
        for i in data:
            pq.insert(i)

        pq.printPQ()
        self.assertEqual(pq.count(), 5)

        m = pq.delMax()
        self.assertEqual(m, 'e')

        pq.printPQ()


    def test_MaxPQ_2(self):
        pq = MaxPQ()

        pq.insert('P')
        pq.insert('Q')
        pq.insert('E')
        self.assertEqual(pq.delMax(), 'Q')

        pq.insert('X')
        pq.insert('A')
        pq.insert('M')
        self.assertEqual(pq.delMax(), 'X')

        pq.insert('P')
        pq.insert('L')
        pq.insert('E')
        self.assertEqual(pq.delMax(), 'P')

        pq.printPQ()


    def test_heap_sort(self):
        data = ['S', 'O', 'R', 'T', 'E', 'X', 'A', 'M', 'P', 'L', 'E']
        sorted_data = heap_sort(data)
        for i in range(len(sorted_data)-1):
            self.assertLessEqual(sorted_data[i], sorted_data[i+1])


if __name__ == '__main__':
    unittest.main()
