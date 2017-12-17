# -*- coding: utf-8 -*-
from collections import deque


"""
What is iterable?
https://stackoverflow.com/questions/9884132/what-exactly-are-pythons-iterator-iterable-and-iteration-protocols

Comparing types
https://dzone.com/articles/comparing-types-in-python-3-1
"""


class Utils():
    @staticmethod
    def lessequal(val1, val2):
        return val1 <= val2


    @staticmethod
    def exchange(datas, index1, index2):
        '''
        https://stackoverflow.com/questions/2493920/how-to-switch-position-of-two-items-in-a-python-list
        '''
        # index() 返回val第一次出现时的索引。
        # val1Index, val2Index = datas.index(val1), datas.index(val2)
        # datas[val1Index], datas[val2Index] = val2, val1
        datas[index1], datas[index2] = datas[index2], datas[index1]


    @staticmethod
    def show(datas):
        print(datas)


    @staticmethod
    def isSorted(datas):
        ret = True
        for i in range(1, len(datas)):
            if Utils.lessequal(datas[i], datas[i-1]):
                ret = False
                break

        return ret


if __name__ == '__main__':
    print(Utils.lessequal(1, 2))
    print(Utils.lessequal(2, 1))
    print(Utils.lessequal(1, 1))
    # print(Utils.less(1, 'a'))

    datas = [0, 1, 2, 3, 5, 4]
    print(Utils.isSorted(datas))
    Utils.exchange(datas, 4, 5)
    print(Utils.isSorted(datas))
    Utils.show(datas)
