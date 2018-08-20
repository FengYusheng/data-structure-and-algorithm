# -*- coding: utf-8 -*-

import unittest

from search import *


class TesstSequentialSearchST(unittest.TestCase):
    def test_isEmpty(self):
        st = SequentialSearchST()
        self.assertTrue(st.isEmpty)


    def test_put_and_get(self):
        data = [('S', 0), ('E', 1), ('A', 2), ('R', 3), ('C', 4), ('H', 5), ('E', 6), ('X', 7),
        ('A', 8), ('M', 9), ('P', 10), ('L', 11), ('E', 12)]

        st = SequentialSearchST()

        for k, v in data:
            st.put(k, v)

        for k, v in [('L', 11), ('P', 10), ('M', 9), ('X', 7), ('H', 5), ('C', 4), ('R', 3), ('A', 8), ('E', 12)]:
            self.assertEqual(st.get(k), v)


    def test_contains(self):
        data = [('S', 0), ('E', 1), ('A', 2), ('R', 3), ('C', 4), ('H', 5), ('E', 6), ('X', 7),
        ('A', 8), ('M', 9), ('P', 10), ('L', 11), ('E', 12)]

        st = SequentialSearchST()

        self.assertFalse(st.contains('M'))

        for k, v in data:
            st.put(k, v)

        self.assertTrue(st.contains('M'))
        self.assertFalse(st.contains('Q'))


    def test_keys(self):
        data = [('S', 0), ('E', 1), ('A', 2), ('R', 3), ('C', 4), ('H', 5), ('E', 6), ('X', 7),
        ('A', 8), ('M', 9), ('P', 10), ('L', 11), ('E', 12)]

        keys = 'SEARCHXMPL'
        i = 0

        st = SequentialSearchST()

        for k, v in data:
            st.put(k, v)

        for k in st.keys():
            self.assertEqual(k, keys[i])
            i += 1


    def test_delete(self):
        data = [('S', 0), ('E', 1), ('A', 2), ('R', 3), ('C', 4), ('H', 5), ('E', 6), ('X', 7),
        ('A', 8), ('M', 9), ('P', 10), ('L', 11), ('E', 12)]

        st = SequentialSearchST()

        for k, v in data:
            st.put(k, v)

        st.delete('M')
        self.assertFalse(st.contains('M'))



class TestBinarySearchST(unittest.TestCase):
    def test_put_and_get(self):
        data = [('S', 0), ('E', 1), ('A', 2), ('R', 3), ('C', 4), ('H', 5), ('E', 6), ('X', 7),
        ('A', 8), ('M', 9), ('P', 10), ('L', 11), ('E', 12)]

        bst = BinarySearchST()

        self.assertTrue(bst.isEmpty())

        for k, v in data:
            bst.put(k, v)

        for k, v in [('L', 11), ('P', 10), ('M', 9), ('X', 7), ('H', 5), ('C', 4), ('R', 3), ('A', 8), ('E', 12)]:
            self.assertEqual(bst.get(k), v)


    def test_rank(self):
        data = [('S', 0), ('E', 1), ('A', 2), ('R', 3), ('C', 4), ('H', 5), ('E', 6), ('X', 7),
        ('A', 8), ('M', 9), ('P', 10), ('L', 11), ('E', 12)]

        bst = BinarySearchST()

        for k, v in data:
            bst.put(k, v)

        self.assertEqual(bst.rank('A'), 0)
        self.assertEqual(bst.rank('L'), 4)
        self.assertEqual(bst.rank('X'), 9)
        self.assertEqual(bst.rank('I'), 4)


    def test_put2(self):
        data = [('S', 0), ('E', 1), ('A', 2), ('R', 3), ('C', 4), ('H', 5), ('E', 6), ('X', 7),
        ('A', 8), ('M', 9), ('P', 10), ('L', 11), ('E', 12)]

        bst = BinarySearchST()

        for k, v in data:
            bst.put2(k, v)

        for k, v in [('L', 11), ('P', 10), ('M', 9), ('X', 7), ('H', 5), ('C', 4), ('R', 3), ('A', 8), ('E', 12)]:
            self.assertEqual(bst.get2(k), v)


    def test_ceiling(self):
        data = [('S', 0), ('E', 1), ('A', 2), ('R', 3), ('C', 4), ('H', 5), ('E', 6), ('X', 7),
        ('A', 8), ('M', 9), ('P', 10), ('L', 11), ('E', 12)]

        bst = BinarySearchST()

        for k, v in data:
            bst.put2(k, v)

        self.assertEqual(bst.ceiling('E'), 'E')
        self.assertEqual(bst.ceiling('I'), 'L')

        self.assertEqual(bst.ceiling2('E'), 'E')
        self.assertEqual(bst.ceiling2('I'), 'L')


    def test_contains(self):
        data = [('S', 0), ('E', 1), ('A', 2), ('R', 3), ('C', 4), ('H', 5), ('E', 6), ('X', 7),
        ('A', 8), ('M', 9), ('P', 10), ('L', 11), ('E', 12)]

        bst = BinarySearchST()

        for k, v in data:
            bst.put2(k, v)

        self.assertTrue(bst.contains('E'))
        self.assertTrue(bst.contains2('E'))
        self.assertFalse(bst.contains('I'))
        self.assertFalse(bst.contains2('I'))


    def test_floor(self):
        data = [('S', 0), ('E', 1), ('A', 2), ('R', 3), ('C', 4), ('H', 5), ('E', 6), ('X', 7),
        ('A', 8), ('M', 9), ('P', 10), ('L', 11), ('E', 12)]

        bst = BinarySearchST()

        for k, v in data:
            bst.put2(k, v)

        self.assertEqual(bst.floor('A'), 'A')
        self.assertEqual(bst.floor('I'), 'H')
        self.assertEqual(bst.floor2('A'), 'A')
        self.assertEqual(bst.floor2('I'), 'H')


class TestBinarySearchTree(unittest.TestCase):
    def test_size(self):
        self.assertEqual(len(BinarySearchTree()), 0)


    def test_put_and_get(self):
        bst = BinarySearchTree()
        data = [('S', 0), ('E', 1), ('A', 2), ('R', 3), ('C', 4), ('H', 5), ('E', 6), ('X', 7),
        ('A', 8), ('M', 9), ('P', 10), ('L', 11), ('E', 12)]

        for key, value in data:
            bst.put(key, value)

        self.assertEqual(len(bst), 10)

        for k, v in [('L', 11), ('P', 10), ('M', 9), ('X', 7), ('H', 5), ('C', 4), ('R', 3), ('A', 8), ('E', 12)]:
            self.assertEqual(bst.get(k), v)


    def test_put2_and_get2(self):
        bst = BinarySearchTree()
        data = [('S', 0), ('E', 1), ('A', 2), ('R', 3), ('C', 4), ('H', 5), ('E', 6), ('X', 7),
        ('A', 8), ('M', 9), ('P', 10), ('L', 11), ('E', 12)]

        for key, value in data:
            bst.put2(key, value)

        self.assertEqual(len(bst), 10)

        for k, v in [('L', 11), ('P', 10), ('M', 9), ('X', 7), ('H', 5), ('C', 4), ('R', 3), ('A', 8), ('E', 12)]:
            self.assertEqual(bst.get2(k), v)


    def test_contains(self):
        bst = BinarySearchTree()
        data = [('S', 0), ('E', 1), ('A', 2), ('R', 3), ('C', 4), ('H', 5), ('E', 6), ('X', 7),
        ('A', 8), ('M', 9), ('P', 10), ('L', 11), ('E', 12)]

        for key, value in data:
            bst.put2(key, value)

        self.assertTrue(bst.contains('A'))
        self.assertTrue(bst.contains2('L'))
        self.assertFalse(bst.contains('I'))
        self.assertFalse(bst.contains2('I'))


    def test_min(self):
        bst = BinarySearchTree()
        data = [('S', 0), ('E', 1), ('A', 2), ('R', 3), ('C', 4), ('H', 5), ('E', 6), ('X', 7),
        ('A', 8), ('M', 9), ('P', 10), ('L', 11), ('E', 12)]

        for key, value in data:
            bst.put2(key, value)

        self.assertEqual(bst.min(), 'A')
        self.assertEqual(bst.min2(), 'A')


    def test_max(self):
        bst = BinarySearchTree()
        data = [('S', 0), ('E', 1), ('A', 2), ('R', 3), ('C', 4), ('H', 5), ('E', 6), ('X', 7),
        ('A', 8), ('M', 9), ('P', 10), ('L', 11), ('E', 12)]

        for key, value in data:
            bst.put2(key, value)

        self.assertEqual(bst.max(), 'X')
        self.assertEqual(bst.max2(), 'X')


    def test_delete_min(self):
        bst = BinarySearchTree()
        data = [('S', 0), ('E', 1), ('A', 2), ('R', 3), ('C', 4), ('H', 5), ('E', 6), ('X', 7),
        ('A', 8), ('M', 9), ('P', 10), ('L', 11), ('E', 12)]

        for key, value in data:
            bst.put2(key, value)

        self.assertEqual(bst.deleteMin(), ('A', 8))
        self.assertEqual(len(bst), 9)


    def test_delete_max(self):
        bst = BinarySearchTree()
        data = [('S', 0), ('E', 1), ('A', 2), ('R', 3), ('C', 4), ('H', 5), ('E', 6), ('X', 7),
        ('A', 8), ('M', 9), ('P', 10), ('L', 11), ('E', 12)]

        for key, value in data:
            bst.put2(key, value)

        self.assertEqual(bst.deleteMax(), ('X', 7))
        self.assertEqual(len(bst), 9)


    def test_delete(self):
        bst = BinarySearchTree()
        data = [('S', 0), ('E', 1), ('A', 2), ('R', 3), ('C', 4), ('H', 5), ('E', 6), ('X', 7),
        ('A', 8), ('M', 9), ('P', 10), ('L', 11), ('E', 12)]

        for key, value in data:
            bst.put2(key, value)

        self.assertEqual(bst.delete('E'), ('E', 12))
        self.assertEqual(len(bst), 9)


    def test_keys(self):
        bst = BinarySearchTree()
        data = [('S', 0), ('E', 1), ('A', 2), ('R', 3), ('C', 4), ('H', 5), ('E', 6), ('X', 7),
        ('A', 8), ('M', 9), ('P', 10), ('L', 11), ('E', 12)]

        for key, value in data:
            bst.put2(key, value)

        print(bst.keys('L', 'P'))
        print(bst.keys())


    def test_ceiling(self):
        bst = BinarySearchTree()
        data = [('S', 0), ('E', 1), ('A', 2), ('R', 3), ('C', 4), ('H', 5), ('E', 6), ('X', 7),
        ('A', 8), ('M', 9), ('P', 10), ('L', 11), ('E', 12)]

        for key, value in data:
            bst.put2(key, value)

        self.assertEqual(bst.ceiling('I'), 'H')
        self.assertEqual(bst.ceiling('L'), 'L')
        self.assertEqual(bst.ceiling('Z'), 'X')
        self.assertEqual(bst.ceiling('B'), 'A')


    def test_floor(self):
        bst = BinarySearchTree()
        data = [('S', 0), ('E', 1), ('A', 2), ('R', 3), ('C', 4), ('H', 5), ('E', 6), ('X', 7),
        ('A', 8), ('M', 9), ('P', 10), ('L', 11), ('E', 12)]

        for key, value in data:
            bst.put2(key, value)

        self.assertEqual(bst.floor('I'), 'L')


    def test_rank(self):
        bst = BinarySearchTree()
        data = [('S', 0), ('E', 1), ('A', 2), ('R', 3), ('C', 4), ('H', 5), ('E', 6), ('X', 7),
        ('A', 8), ('M', 9), ('P', 10), ('L', 11), ('E', 12)]

        for key, value in data:
            bst.put2(key, value)

        self.assertEqual(bst.rank('A'), 0)
        self.assertEqual(bst.rank('X'), 9)
        self.assertEqual(bst.rank('Z'), 10)


    def test_select(self):
        bst = BinarySearchTree()
        data = [('S', 0), ('E', 1), ('A', 2), ('R', 3), ('C', 4), ('H', 5), ('E', 6), ('X', 7),
        ('A', 8), ('M', 9), ('P', 10), ('L', 11), ('E', 12)]

        for key, value in data:
            bst.put2(key, value)

        self.assertEqual(bst.select(0), 'A')
        self.assertEqual(bst.select(1), 'C')


    def test_height(self):
        bst = BinarySearchTree()
        data = [('S', 0), ('E', 1), ('A', 2), ('R', 3), ('C', 4), ('H', 5), ('E', 6), ('X', 7),
        ('A', 8), ('M', 9), ('P', 10), ('L', 11), ('E', 12)]

        for key, value in data:
            bst.put2(key, value)

        self.assertEqual(bst.height(), 5)


    def test_level_order(self):
        bst = BinarySearchTree()
        data = [('S', 0), ('E', 1), ('A', 2), ('R', 3), ('C', 4), ('H', 5), ('E', 6), ('X', 7),
        ('A', 8), ('M', 9), ('P', 10), ('L', 11), ('E', 12)]

        for key, value in data:
            bst.put2(key, value)

        print(bst.levelOrder())



class TestRedBlackBST(unittest.TestCase):
    def test_empty_tree(self):
        rbt = RedBlackBST()
        self.assertEqual(len(rbt), 0)


    def test_level_order(self):
        rbt = RedBlackBST()
        data = [('S', 0), ('E', 1), ('A', 2), ('R', 3), ('C', 4), ('H', 5), ('E', 6), ('X', 7),
        ('A', 8), ('M', 9), ('P', 10), ('L', 11), ('E', 12)]

        for key, value in data:
            rbt.put(key, value)

        print(rbt.levelOrder())


    def test_level_order2(self):
        rbt = RedBlackBST()
        data = [('A', 0), ('C', 1), ('E', 2), ('H', 3), ('L', 4), ('M', 5), ('P', 6), ('R', 7), ('S', 8), ('X', 9)]

        for key, value in data:
            rbt.put(key, value)

        print(rbt.levelOrder())


    def test_height(self):
        rbt = RedBlackBST()
        data = [('A', 0), ('C', 1), ('E', 2), ('H', 3), ('L', 4), ('M', 5), ('P', 6), ('R', 7), ('S', 8), ('X', 9)]

        for key, value in data:
            rbt.put(key, value)

        self.assertEqual(rbt.height(), 3)


    def test_get(self):
        rbt = RedBlackBST()
        data = [('S', 0), ('E', 1), ('A', 2), ('R', 3), ('C', 4), ('H', 5), ('E', 6), ('X', 7),
        ('A', 8), ('M', 9), ('P', 10), ('L', 11), ('E', 12)]

        for key, value in data:
            rbt.put(key, value)

        self.assertEqual(rbt.get('E'), 12)
        self.assertIsNone(rbt.get('Q'))


if __name__ == '__main__':
    unittest.main()
