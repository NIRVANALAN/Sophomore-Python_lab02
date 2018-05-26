'''
4 现在想将常用的排序算法封装成一个算法工具类SortLib，请尝试实现。要求：
(1) 	至少包含1种排序算法（如：冒泡排序）。
(2) 	随机生成一个含20个整数的列表，来测试实现的工具类SortLib。
'''

import random
from copy import copy


class SortLib:

    def directInsertSort(self, seq):
        """ 直接插入排序 """
        size = len(seq)
        for i in range(1, size):
            tmp, j = seq[i], i
            while j > 0 and tmp < seq[j - 1]:
                seq[j], j = seq[j - 1], j - 1
            seq[j] = tmp
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
            l[i], l[k] = l[k], l[i]
        # print(l)
        return l

    def bubbleSort(self, seq):
        """冒泡排序"""
        size = len(seq)
        for i in range(1, size):
            for j in range(0, size - i):
                if seq[j + 1] < seq[j]:
                    seq[j + 1], seq[j] = seq[j], seq[j + 1]
        return seq

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
        """快速排序辅助函数"""
        if low >= high:
            return
        mid = self._divide(seq, low, high)
        self._quickSort(seq, low, mid - 1)
        self._quickSort(seq, mid + 1, high)

    def quickSort(self, seq):
        """快速排序包裹函数"""
        size = len(seq)
        self._quickSort(seq, 0, size - 1)
        return seq

    def merge(self, seq, left, mid, right):
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
            self._mergeSort(seq, left, mid)
            self._mergeSort(seq, mid + 1, right)
            self.merge(seq, left, mid + 1, right)


if __name__ == '__main__':
    from time import clock
    S = SortLib()
    s = []
    for i in range(0, 100):
        s.append(random.randint(1, 50))
    print(s)
    print("\n")
    print("直接选择排序结果：")
    print(S.directSelectSort(copy(s)))
    print("直接插入排序结果：")
    print(S.directInsertSort(copy(s)))
    print("冒泡排序结果：")
    start = clock()
    print(S.bubbleSort(copy(s)))
    finish = clock()
    print(finish - start)
    print("快速排序结果：")
    start = clock()
    print(S.quickSort(copy(s)))
    finish = clock()
    print(finish - start)
