'''
4 现在想将常用的排序算法封装成一个算法工具类SortLib，请尝试实现。要求：
(1) 	至少包含1种排序算法（如：冒泡排序）。
(2) 	随机生成一个含20个整数的列表，来测试实现的工具类SortLib。
'''

import random
from copy import copy
from time import clock


class SortLib:

    def directInsertSort(self, seq):
        """ InsertSort  """
        size = len(seq)
        for i in range(1, size):
            tmp, j = seq[i], i - 1
            while j >= 0 and tmp < seq[j]:
                seq[j + 1], j = seq[j], j - 1
            seq[j + 1] = tmp
        return seq

    def InsertionSortdichotomy(self, seq):
        '''locate with dichotomy search'''
        size = len(seq)
        for i in range(1, size):
            get = seq[i]
            left = 0
            right = i 
            while left < right:
                mid = (int)((left + right) / 2)
                if seq[mid] > get:
                    right = mid - 1
                else:
                    left = mid + 1
            j = i - 1
            while j >= left:
                seq[j + 1] = seq[j]
                j -= 1
            seq[left] = get
        return seq

    def selectSort(self, l):
        '''select sort 选择排序'''
        size = len(l) - 1
        for i in range(size):
            k = i
            j = i + 1
            while j <= size:
                if l[k] > l[j]:
                    k = j
                j += 1
            l[i], l[k] = l[k], l[i]  # swap via tuple
        # print(l)
        return l

    def bubbleSort(self, l):
        """冒泡排序"""
        size = len(l)
        for i in range(1, size):
            for j in range(0, size - i):
                if l[j + 1] < l[j]:
                    l[j + 1], l[j] = l[j], l[j + 1]
        return l

    def _divide(self, seq, low, high):
        """快速排序划分函数"""
        tmp = seq[low]
        while low != high:
            while low < high and seq[high] >= tmp:
                high -= 1
            if low < high:
                seq[low] = seq[high]
                low += 1
            while low < high and seq[low] <= tmp:
                low += 1
            if low < high:
                seq[high] = seq[low]
                high -= 1
        seq[low] = tmp
        return low

    def _quickSort(self, seq, low, high):
        """quicksort assist"""
        if low >= high:
            return
        mid = self._divide(seq, low, high)
        self._quickSort(seq, low, mid - 1)
        self._quickSort(seq, mid + 1, high)

    def quickSort(self, seq):
        """quicksort"""
        size = len(seq)
        self._quickSort(seq, 0, size - 1)
        return seq

    def merge(self, seq, left, mid, right):
        '''merge sort'''
        tmp = []
        i, j = left, mid
        while i < mid and j <= right:
            if seq[i] < seq[j]:
                tmp.append(seq[i])
                i += 1
            else:
                tmp.append(seq[j])
                j += 1
        if i < mid:
            tmp.extend(seq[i:])
        if j <= right:
            tmp.extend(seq[j:])

        seq[left:right + 1] = tmp[0:right - left + 1]

    def _mergeSort(self, seq, left, right):
        if left == right:
            return
        else:
            mid = (left + right) / 2
            self._mergeSort(seq, left, mid)  # recursive
            self._mergeSort(seq, mid + 1, right)
            self.merge(seq, left, mid + 1, right)


if __name__ == '__main__':
    S = SortLib()
    s = []
    for i in range(0, 100):
        s.append(random.randint(1, 100))
    print("初始无序队列", s)
    print("\n")
    print("直接选择排序结果：")
    print(S.selectSort(copy(s)))
    print("直接插入排序结果：")
    print(S.directInsertSort(copy(s)))
    print("二分插入排序结果")
    print(S.InsertionSortdichotomy(copy(s)))
    print("冒泡排序结果：")
    start = clock()
    print(S.bubbleSort(copy(s)))
    finish = clock()
    print(finish - start)
    print("快速排序结果：")
    start = clock()
    print(S.quickSort(copy(s)))
    finish = clock()
    print('finished in:', finish - start)
