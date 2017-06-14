# -*- coding: utf-8 -*-

#---------------------------------------
#   程序：选择排序
#   作者：Yuwei Meng
#   日期：2017-06-14
#   语言：Python 3.6
#   说明：选择排序的简单实现
#---------------------------------------


def select_sort(ary):
    n = len(ary)
    for i in range(0, n):
        min = i  # 最小元素下标标记
        for j in range(i + 1, n):
            if ary[j] < ary[min]:
                min = j  # 找到最小值的下标
        ary[min], ary[i] = ary[i], ary[min]  # 交换两者
    return ary
