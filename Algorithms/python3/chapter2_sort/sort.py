# -*- coding: utf-8 -*-
import copy

from common import Utils


def selectionSort(datas=[]):
    """
    这种排序总是不断地从剩余元素中选择最小者。

    优点：
        这种排序的数据移动次数是最少的，交换次数和数组大小是线性关系。其他任何算法都不具备这种
        特征，大部分的数量级是线性对数或是平方级别。比较的次数是平方级别的。

    缺点：
        运行时间和输入无关，一个有序的数组或是主键完全相同的数组和一个元素随机排列的数组所用的
        时间一样。
    """
    pivot = 0
    length = len(datas)
    while pivot < length:
        miniIndex = pivot
        for index in range(pivot+1, length):
            if not Utils.lessequal(datas[miniIndex], datas[index]):
                miniIndex = index

        Utils.exchange(datas, pivot, miniIndex)
        pivot += 1



def insertionSort(datas=[]):
    """
    将新来的元素插入到已经有序的数组中。插入排序的时间取决于输入元素的原始顺序。插入排序对部分
    有序的数组很有效：
        １．数组中每个元素距离它的最终位置都不远；
        ２．一个有序的大数组接一个小数组；
        ３．数组中只有几个元素的位置不正确。
    当倒置的数量很少时，插入排序可能比其基础他排序更快。
    """
    length = len(datas)
    if length > 1:
        for pivot in range(1, length):
            for index in range(0, pivot)[::-1]:
                if not Utils.lessequal(datas[index], datas[pivot]):
                    Utils.exchange(datas, pivot, index)
                    pivot = index
                else:
                    break


def shellSort(datas=[]):
    """
    增强版的插入排序，逐步将原始数组变成局部有序的数组，最后用插入排序。
    当你不清楚用什么排序算法对一个原始数组合适时，就先用shell sort. 这种算法实现简单，对于一
    般的大数组它的用时也是可以接受的。
    """
    length = len(datas)
    h = 0
    while h < length/3:
        h = 3 * h + 1

    while h >= 1: # The last loop runs a insertion sort.
        for pivot in range(h, length):
            for index in range(0, pivot)[::-h]:
                if not Utils.lessequal(datas[index], datas[pivot]):
                    Utils.exchange(datas, pivot, index)
                    pivot = index
                else:
                    break

        h = int(h/3) # h/3 returns a float number.


def mergeSort(datas=[]):
    """
    优点：
        任意长度为Ｎ的数组归并排序所需的时间和NlogN成正比，可以用归并排序百万级的数据。
    缺点：
        归并排序所需的额外空间和Ｎ成正比。
    """
    def _merge(_data, lo, mid, hi):
        auxiliary = copy.copy(_data)
        _lo = lo
        _hi = mid + 1
        for i in range(lo, hi+1):
            if _lo > mid:
                _data[i] = auxiliary[_hi]
                _hi += 1
            elif _hi > hi:
                _data[i] = auxiliary[_lo]
                _lo += 1
            elif Utils.lessequal(auxiliary[_lo], auxiliary[_hi]):
                _data[i] = auxiliary[_lo]
                _lo += 1
            else:
                _data[i] = auxiliary[_hi]
                _hi += 1

    def _mergeSort(_data, lo, hi):
        if hi <= lo:
            return

        mid = lo + int((hi-lo)/2)
        _mergeSort(_data, lo, mid)
        _mergeSort(_data, mid+1, hi)
        _merge(_data, lo, mid, hi)

    lo = 0
    hi = len(datas) - 1
    _mergeSort(datas, lo, hi)



if __name__ == '__main__':
    datas = ['S', 'O', 'R', 'T', 'E', 'X', 'A', 'M', 'P', 'L', 'E']
    mergeData = ['E', 'E', 'G', 'M', 'R', 'A', 'C', 'E', 'R', 'T']
    mergeSortData = ['M', 'E', 'R', 'G', 'S', 'O', 'R', 'T', 'E', 'X', 'A', 'M', 'P', 'L', 'E']
    # selectionSort(datas)
    # insertionSort(datas)
    # shellSort(datas)
    mergeSort(mergeSortData)
    Utils.show(mergeSortData)
