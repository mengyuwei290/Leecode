# -*- coding: utf-8 -*-

#---------------------------------------
#   程序：插入排序
#   作者：Yuwei Meng
#   日期：2017-06-14
#   语言：Python 3.6
#   说明：步长的选择是从n/2开始，每次再减半，直至为0
#---------------------------------------


def shell_sort(ary):
    n = len(ary)
    gap = round(n / 2)  # 初始步长 , 用round四舍五入取整
    while gap > 0:
        for i in range(gap, n):  # 每一列进行插入排序 , 从gap 到 n-1
            temp, j = ary[i], i
            while (j >= gap and ary[j - gap] > temp):  # 插入排序
                ary[j] = ary[j - gap]
                j = j - gap
            ary[j] = temp
        gap = round(gap / 2)  # 重新设置步长
    return ary
