# -*- coding: utf-8 -*-
from collections import deque


class Node:
    def __init__(self, key, value, next=None):
        self.value = value
        self.key = key
        self.next = next


    def __next__(self):
        return self.next


    def item(self):
        return self.value


    def setItem(self, value):
        self.value = value


    def gettKey(self):
        return self.key


    def setNext(self, next):
        self.next = next


class SequentialSearchST:
    def __init__(self):
        self.head = Node('head', None)
        self.size = 0


    def __iter__(self):
        pivot = self.head

        while next(pivot) is not None:
            yield next(pivot)
            pivot = next(pivot)


    def __str__(self):
        return str([(i.gettKey(), i.item()) for i in self])


    def isEmpty(self):
        return self.size == 0


    def get(self, key):
        pivot = self.head
        val = None

        while next(pivot) is not None:
            pivot = next(pivot)
            if pivot.gettKey() == key:
                val = pivot.item()
                break

        return val


    def put(self, key, value):
        pivot = self.head
        while next(pivot) is not None:
            pivot = next(pivot)
            if pivot.gettKey() == key:
                pivot.setItem(value)
                break

        next(pivot) is None and pivot.gettKey() != key and pivot.setNext(Node(key, value))

        self.size += 1


    def delete(self, key):
        pivot = self.head

        while pivot is not None:
            if next(pivot).gettKey() == key:
                pivot.setNext(next(next(pivot)))
                break

            pivot = next(pivot)


    def contains(self, key):
        existing = False

        for n in self:
            if n.gettKey() == key:
                existing = True
                break

        return existing


    def keys(self):
        return (i.gettKey() for i in self)



class BinarySearchST:
    def __init__(self):
        self.keys = deque()
        self.values = deque()


    def size(self):
        return len(self.keys)


    def isEmpty(self):
        return self.size() == 0


    def rank(self, key):
        """The result is larger than or equal to the key"""
        mid = lo = 0
        hi = self.size() - 1

        # "lo <= hi". The key on the lelf of lo is less than the given key. And The key on the right of the hi is larger than the given key.
        while lo <= hi:
            # This sentence causes an infinite loop.
            # mid = int(self.size()/2) if self.size()%2 > 0 else int(self.size()/2-1)
            mid = lo + int((hi-lo)/2)

            if self.keys[mid] < key:
                lo = mid + 1
            elif self.keys[mid] > key:
                hi = mid - 1
            else:
                break

        return mid if lo <= hi else lo


    def put(self, key, value):
        # NOTE: The performance of "put" is slow.
        pivot = self.size() - 1

        while pivot >= 0:
            if self.keys[pivot] == key:
                self.values[pivot] = value
                break

            pivot -= 1

        # keys doesn't exists in the queue, and insert it into an appropriate position.
        if pivot < 0:
            # Insertion sort
            self.keys.append(key)
            self.values.append(value)

            pivot = self.size() - 1

            while pivot - 1 >= 0:
                if self.keys[pivot-1] > self.keys[pivot]:
                    self.keys[pivot-1], self.keys[pivot] = self.keys[pivot], self.keys[pivot-1]
                    self.values[pivot-1], self.values[pivot] = self.values[pivot], self.values[pivot-1]
                    pivot -= 1
                else:
                    break


    def put2(self, key, value):
        pivot = self.rank(key)
        if pivot < self.size() and self.keys[pivot] == key:
            self.values[pivot] = value
            return

        self.keys.append('-')
        self.values.append('-')
        j = self.size() - 1

        while j > pivot:
            self.keys[j], self.values[j] = self.keys[j-1], self.values[j-1]
            j -= 1

        self.keys[pivot], self.values[pivot] = key, value


    def get(self, key):
        value = None
        pivot = 0

        if not self.isEmpty():
            while pivot < self.size():
                if self.keys[pivot] == key:
                    value = self.values[pivot]
                    break

                pivot += 1

        return value


    def get2(self, key):
        pos = self.rank(key)
        return self.values[pos] if pos < self.size() and self.keys[pos] == key else None


    def display(self):
        for i in range(self.size()):
            print(self.keys[i], self.values[i])


    def ceiling(self, key):
        """Returns the smallest key in this symbol table greater than or equal to key."""
        result = None

        for k in self.keys:
            if k >= key:
                result = k
                break

        return result


    def ceiling2(self, key):
        """Returns the smallest key in this symbol table greater than or equal to key."""
        pos = self.rank(key)
        return self.keys[pos] if pos < self.size() else None


    def contains(self, key):
        existing = False

        for k in self.keys:
            if k == key:
                existing = True
                break

        return existing


    def contains2(self, key):
        pos = self.rank(key)
        return self.keys[pos] == key if pos < self.size() else False


    def floor(self, key):
        result = None

        for i in self.keys:
            if i <= key:
                result = i
            else:
                break

        return result


    def floor2(self, key):
        pos = self.rank(key)
        return self.keys[pos] if pos < self.size() and self.keys[pos] <= key else self.keys[pos-1]



class Leaf:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None


    def __len__(self):
        size = 1

        if self.left is not None:
            size = size + len(self.left)

        if self.right is not None:
            size = size + len(self.right)

        return size


    def getKey(self):
        return self.key


    def setKey(self, key):
        self.key = key


    def item(self):
        return self.value


    def setItem(self, value):
        self.value = value


    def getLeftSubtree(self):
        return self.left


    def getRightSubtree(self):
        return self.right


    def setLeftSubtree(self, substree):
        self.left = substree


    def setRightSubtree(self, substree):
        self.right = substree



class BinarySearchTree:
    def __init__(self, root=None):
        self.root = root


    def __len__(self):
        return len(self.root) if self.root is not None else 0


    def put(self, key, value):
        def _put(pivot):
            tree = pivot
            if pivot is None:
                tree = Leaf(key, value)
            elif pivot.getKey() == key:
                pivot.setItem(value)
            elif pivot.getKey() > key:
                pivot.setLeftSubtree(_put(pivot.getLeftSubtree()))
            else:
                pivot.setRightSubtree(_put(pivot.getRightSubtree()))

            return tree

        self.root = _put(self.root)


    def put2(self, key, value):
        pivot, parent = self.root, None

        while pivot is not None:
            if pivot.getKey() == key:
                pivot.setItem(value)
                break
            elif pivot.getKey() > key:
                parent = pivot
                pivot = pivot.getLeftSubtree()
            else:
                parent = pivot
                pivot = pivot.getRightSubtree()

        if parent is None and pivot is None:
            self.root = Leaf(key, value)
        elif pivot is None:
            # "parent.getKey() > key and parent.setLeftSubtree(Leaf(key, value))" returns None
            # This means the sentence will be run after "or" every time.
            # parent.getKey() > key and parent.setLeftSubtree(Leaf(key, value)) or parent.setRightSubtree(Leaf(key, value)

            # if parent.getKey() > key:
            #     parent.setLeftSubtree(Leaf(key, value))
            # else:
            #     parent.setRightSubtree(Leaf(key, value))

             parent.getKey() > key and (parent.setLeftSubtree(Leaf(key, value)), True) or parent.setRightSubtree(Leaf(key, value))


    def get(self, key):
        def _get(pivot):
            result = None

            if pivot is not None:
                if pivot.getKey() == key:
                    result = pivot.item()
                elif pivot.getKey() > key:
                    result = _get(pivot.getLeftSubtree())
                else:
                    result = _get(pivot.getRightSubtree())

            return result

        return _get(self.root)


    def get2(self, key):
        result, pivot = None, self.root

        while pivot is not None:
            if pivot.getKey() == key:
                result = pivot.item()
                break
            elif pivot.getKey() > key:
                pivot = pivot.getLeftSubtree()
            else:
                pivot = pivot.getRightSubtree()

        return result


    def contains(self, key):
        pivot = self.root
        existing = False

        while pivot is not None:
            if pivot.getKey() == key:
                existing = True
                break
            elif pivot.getKey() > key:
                pivot = pivot.getLeftSubtree()
            else:
                pivot = pivot.getRightSubtree()

        return existing


    def contains2(self, key):
        return self.get(key) is not None


    def min(self):
        result, pivot = None, self.root

        if self.root is not None:
            while pivot.getLeftSubtree() is not None:
                pivot = pivot.getLeftSubtree()

            if pivot is not None:
                result = pivot.getKey()

        return result


    def min2(self):
        def _min(pivot):
            result = None

            if pivot is not None:
                if pivot.getLeftSubtree() is not None:
                    result = _min(pivot.getLeftSubtree())
                else:
                    result = pivot.getKey()

            return result


        return _min(self.root)


    def max(self):
        result, pivot = None, self.root

        if self.root is not None:
            while pivot.getRightSubtree() is not None:
                pivot = pivot.getRightSubtree()

            if pivot.getRightSubtree() is None:
                result = pivot.getKey()

        return result


    def max2(self):
        def _max(pivot):
            result = None

            if self.root is not None:
                if pivot.getRightSubtree() is not None:
                    result = _max(pivot.getRightSubtree())
                else:
                    result = pivot.getKey()

            return result

        return _max(self.root)


    def deleteMax(self):
        parent = result = None
        pivot = self.root

        if self.root is not None:
            while pivot.getRightSubtree() is not None:
                parent = pivot
                pivot = pivot.getRightSubtree()

            result = (pivot.getKey(), pivot.item())
            parent.setRightSubtree(pivot.getLeftSubtree())

        return result


    def deleteMin(self, substree=None):
        parent = result = None
        pivot = self.root if substree is None else substree

        if pivot is not None:
            while pivot.getLeftSubtree() is not None:
                parent, pivot = pivot, pivot.getLeftSubtree()

            result = (pivot.getKey(), pivot.item())
            parent.setLeftSubtree(pivot.getRightSubtree())

        return result


    def delete(self, key):
        pivot = self.root
        parent = result = None

        while pivot is not None:
            if pivot.getKey() > key:
                parent = pivot
                pivot = pivot.getLeftSubtree()
            elif pivot.getKey() < key:
                parent = pivot
                pivot = pivot.getRightSubtree()
            else:
                result = (pivot.getKey(), pivot.item())
                k, v = self.deleteMin(pivot.getRightSubtree())
                pivot.setKey(k)
                pivot.setItem(v)
                break

        return result


    def keys(self, lo=None, hi=None):
        def _enqueue(pivot):
            if pivot is not None:
                _enqueue(pivot.getLeftSubtree())
                pivot.getKey() >= lo and pivot.getKey() <= hi and queue.append(pivot.getKey())
                _enqueue(pivot.getRightSubtree())

        lo = self.min() if lo is None or self.min() > lo else lo
        hi = self.max() if hi is None or self.max() < hi else hi
        queue = deque()

        _enqueue(self.root)

        return queue


    def travel(self):
        def _travle(pivot):
            if pivot is not None:
                _travle(pivot.getLeftSubtree())
                print(pivot.getKey())
                _travle(pivot.getRightSubtree())

        _travle(self.root)


    def ceiling(self, key):
        def _ceiling(pivot):
            result = None

            if pivot is not None and pivot.getKey() <= key:
                # Try to find out a likely larger key.
                temp = _ceiling(pivot.getRightSubtree())

                result = temp if temp is not None else pivot.getKey()
            elif pivot is not None and pivot.getKey() > key:
                result = _ceiling(pivot.getLeftSubtree())

            return result

        return _ceiling(self.root) if self.root is not None else None


    def floor(self, key):
        def _floor(pivot):
            result = None

            if pivot is not None and pivot.getKey() >= key:
                temp = _floor(pivot.getLeftSubtree())
                result = temp if temp is not None else pivot.getKey()
            elif pivot is not None and pivot.getKey() < key:
                result = _floor(pivot.getRightSubtree())

            return result

        return _floor(self.root) if self.root is not None else None


    def rank(self, key):
        def _length(substree):
            return len(substree) if substree is not None else 0

        def _rank(pivot):
            result = 0

            if pivot is None:
                result = 0
            elif pivot.getKey() == key:
                result = _length(pivot.getLeftSubtree())
            elif pivot.getKey() > key:
                result = _rank(pivot.getLeftSubtree())
            else:
                result = 1 + _length(pivot.getLeftSubtree()) + _rank(pivot.getRightSubtree())

            return result

        return _rank(self.root)


    def select(self, rank):
        """Return the key at postition rank. In other words, rank means there are rank keys at left of the target key."""
        def _length(substree):
            return len(substree) if substree is not None else 0

        def _select(pivot, _rank):
            result = None

            if pivot is not None:
                left_length = _length(pivot.getLeftSubtree())

                if left_length == _rank:
                    result = pivot.getKey()
                elif left_length > _rank:
                    result = _select(pivot.getLeftSubtree(), _rank)
                else:
                    result = _select(pivot.getRightSubtree(), _rank-left_length-1)

            return result

        if self.root is None or len(self.root) < rank:
            return None

        return _select(self.root, rank)


    def height(self):
        """Deep first travel."""
        def _height(pivot):
            result = -1

            if pivot is not None:
                result = 1 + max([_height(pivot.getLeftSubtree()), _height(pivot.getRightSubtree())])

            return result

        return _height(self.root)


    def levelOrder(self):
        """Broad first travel."""
        keys = deque()
        queue = deque()
        if self.root is not None:
            pivot = self.root
            queue.append(pivot)

            while len(queue) > 0:
                pivot = queue.popleft()

                if pivot is not None:
                    keys.append(pivot.getKey())
                    queue.append(pivot.getLeftSubtree())
                    queue.append(pivot.getRightSubtree())

        return keys



class LeafOnRedBlackTree:
    RED = True
    BLACK = False


    def __init__(self, key, value):
        self.key = key
        self.value = value
        self._color = LeafOnRedBlackTree.RED
        self.left = None
        self.right = None


    def __len__(self):
        size = 1

        if self.left is not None:
            size = size + len(self.left)

        if self.right is not None:
            size = size + len(self.right)

        return size


    def setColor(self, color):
        self._color = color


    def color(self):
        return self._color


    def isRed(self):
        return self.color == LeafOnRedBlackTree.RED


    def setKey(self, key):
        self.key = key


    def setItem(self, value):
        self.value = value


    def getKey(self):
        return self.key


    def getItem(self):
        return self.value


    def getLeftSubtree(self):
        return self.left


    def getRightSubtree(self):
        return self.right


    def setLeftSubtree(self, substree):
        self.left = substree


    def setRightSubtree(self, substree):
        self.right = substree



class RedBlackBST:
    def __init__(self, root=None):
        self.root = root


    def __len__(self):
        return len(self.root) if self.root is not None else 0


    @staticmethod
    def isRed(pivot):
        if pivot is None:
            return False

        return hasattr(pivot, 'color') and pivot.color() == LeafOnRedBlackTree.RED


    @staticmethod
    def rotateRight(pivot):
        assert pivot is not None, "pivot is None."
        assert isinstance(pivot, LeafOnRedBlackTree), "pivot is not an instance of LeafOnRedBlackTree."
        assert pivot.getLeftSubtree() is not None, "pivot has no left substree."

        x = pivot.getLeftSubtree()
        pivot.setLeftSubtree(x.getRightSubtree())
        x.setRightSubtree(pivot)
        x.setColor(pivot.color())
        pivot.setColor(LeafOnRedBlackTree.RED)

        return x


    @staticmethod
    def rotateLeft(pivot):
        assert pivot is not None, "pivot is None."
        assert isinstance(pivot, LeafOnRedBlackTree), "pivot is not an instance of LeafOnRedBlackTree."
        assert pivot.getRightSubtree() is not None, "pivot has not right substree."

        x = pivot.getRightSubtree()
        pivot.setRightSubtree(x.getLeftSubtree())
        x.setLeftSubtree(pivot)
        x.setColor(pivot.color())
        pivot.setColor(LeafOnRedBlackTree.RED)

        return x


    @staticmethod
    def flipColor(pivot):
        assert isinstance(pivot, LeafOnRedBlackTree), "pivot is not an instance of LeafOnRedBlackTree."

        RedBlackBST.isRed(pivot) and pivot.setColor(LeafOnRedBlackTree.BLACK)


    def levelOrder(self):
        keys = []
        queue = deque()
        queue.append(self.root)

        while len(queue) > 0:
            pivot = queue.popleft()
            if pivot is not None:
                keys.append(pivot.getKey())
                queue.append(pivot.getLeftSubtree())
                queue.append(pivot.getRightSubtree())

        return keys


    def height(self):
        def _height(pivot):
            high = -1

            if pivot is not None:
                high = 1 + max(_height(pivot.getLeftSubtree()), _height(pivot.getRightSubtree()))

            return high

        return _height(self.root)


    def put(self, key, value):
        def _put(pivot):
            if pivot is None:
                pivot = LeafOnRedBlackTree(key, value)
            elif pivot.getKey() == key:
                pivot.setItem(value)
            elif pivot.getKey() > key:
                pivot.setLeftSubtree(_put(pivot.getLeftSubtree()))
            else:
                pivot.setRightSubtree(_put(pivot.getRightSubtree()))

            if RedBlackBST.isRed(pivot.getRightSubtree()) and not RedBlackBST.isRed(pivot.getLeftSubtree):
                pivot = self.rotateLeft(pivot)

            if self.isRed(pivot.getLeftSubtree()) and self.isRed(pivot.getLeftSubtree().getLeftSubtree()):
                pivot = self.rotateRight(pivot)

            if self.isRed(pivot.getLeftSubtree()) and self.isRed(pivot.getRightSubtree()):
                pivot.getLeftSubtree().setColor(LeafOnRedBlackTree.BLACK)
                pivot.getRightSubtree().setColor(LeafOnRedBlackTree.BLACK)
                pivot.setColor(LeafOnRedBlackTree.RED)

            return pivot

        self.root = _put(self.root)
        RedBlackBST.flipColor(self.root)


    def get(self, key):
        def _get(pivot):
            result = None

            if pivot is not None:
                if pivot.getKey() == key:
                    result = pivot.getItem()
                elif pivot.getKey() > key:
                    result = _get(pivot.getLeftSubtree())
                else:
                    result = _get(pivot.getRightSubtree())

            return result

        return _get(self.root)


    def deleteMin(self):
        """
        """
        def _deleteMin(pivot):
            pass

        return _deleteMin(self.root)


    def deleteMax(self):
        def _deleteMax(pivot):
            pass

        return _deleteMax(self.root)



class HashTable:
    def __init__(self):
        pass



__all__ = [
    'SequentialSearchST',
    'BinarySearchST',
    'BinarySearchTree',
    'RedBlackBST'
]
