# -*- coding: utf-8 -*-

#---------------------------------------
#   程序：归并排序
#   作者：Yuwei Meng
#   日期：2017-06-14
#   语言：Python 3.6
#   说明：归并排序的简单实现
#---------------------------------------


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)


def merge(left, right):
    l, r, res = 0, 0, []
    while l < len(left) and r < len(right):
        if left[l] <= right[r]:
            res.append(left[l])
            l += 1
        else:
            res.append(right[r])
            r += 1
    res += left[l:]
    res += right[r:]
    return res


if __name__ == '__main__':
    arr = [2, 5, 67, 3, 232, 4, 99, 20]
    print(sorted(arr) == merge_sort(arr))
