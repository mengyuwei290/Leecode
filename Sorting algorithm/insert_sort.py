# -*- coding: utf-8 -*-

#---------------------------------------
#   程序：插入排序
#   作者：Yuwei Meng
#   日期：2017-06-14
#   语言：Python 3.6
#   说明：插入排序的简单实现
#---------------------------------------


def insert_sort(arr):
    n = len(arr)
    for i in range(1, n):
        if arr[i] < arr[i - 1]:
            temp, index = arr[i], i
            for j in range(i - 1, -1, -1):
                if arr[j] > temp:
                    arr[j + 1], index = arr[j], j
                else:
                    break
            arr[index] = temp
    return arr
