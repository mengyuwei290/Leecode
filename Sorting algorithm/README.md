经典排序算法在面试中占有很大的比重，也是基础，在这总结一下当下比较经典的排序算法包括冒泡排序，插入排序，选择排序，希尔排序，归并排序，快速排序，堆排序.

##一. 冒泡排序

###步骤:
- 比较相邻的元素。如果第一个比第二个大，就交换他们两个
- 对第0个到第n-1个数据做同样的工作。这时，最大的数就“浮”到了数组最后的位置上
- 针对所有的元素重复以上的步骤，除了最后一个
- 持续每次对越来越少的元素重复上面的步骤，直到没有任何一对数字需要比较

###源码(python):
```
def bubble_sort1(ary):
    n = len(ary)  # 获得数组的长度
    for i in range(n):
        for j in range(1, n - i):
            if ary[j - 1] > ary[j]:  # 如果前者比后者大
                ary[j - 1], ary[j] = ary[j], ary[j - 1]  # 则交换两者
    return ary
```

在这里有两点时可以进行优化的(代码中有):

- 优化1：某一趟遍历如果没有数据交换，则说明已经排好序了，因此不用再进行迭代了。用一个标记记录这个状态即可。
- 优化2：记录某次遍历时最后发生数据交换的位置，这个位置之后的数据显然已经有序，不用再排序了。因此通过记录最后发生数据交换的位置就可以确定下次循环的范围

##二. 选择排序 SelectionSort

###步骤:
- 在未排序序列中找到最小（大）元素，存放到排序序列的起始位置
- 再从剩余未排序元素中继续寻找最小（大）元素，然后放到已排序序列的末尾
- 以此类推，直到所有元素均排序完毕

###源码(python):
```
def select_sort(ary):
    n = len(ary)
    for i in range(0,n):
        min = i                             #最小元素下标标记
        for j in range(i+1,n):
            if ary[j] < ary[min] :
                min = j                     #找到最小值的下标
        ary[min],ary[i] = ary[i],ary[min]   #交换两者
    return ary
```

##三. 插入排序 InsertionSort

###步骤:
- 从第一个元素开始，该元素可以认为已经被排序
- 取出下一个元素，在已经排序的元素序列中从后向前扫描
- 如果被扫描的元素（已排序）大于新元素，将该元素后移一位
- 重复步骤3，直到找到已排序的元素小于或者等于新元素的位置
- 将新元素插入到该位置后
- 重复步骤2~5

###源码(python):
```
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
```

##四. 希尔排序 ShellSort

###步骤:
- 选择一个增量序列t1，t2，…，tk，其中ti>tj，tk=1
- 按增量序列个数k，对序列进行k 趟排序
- 每趟排序，根据对应的增量ti，将待排序列分割成若干长度为m 的子序列，分别对各子表进行直接插入排序。仅增量因子为1 时，整个序列作为一个表来处理，表长度即为整个序列的长度。

###源码(python):
```
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
```

##五. 归并排序 MergeSort

归并排序是采用分治法的一个非常典型的应用。归并排序的思想就是先递归分解数组，再合并数组。

###步骤:
- 合并数组merge:
    - 是比较两个数组的最前面的数，谁小就先取谁，取了后相应的指针就往后移一位
    - 然后再比较，直至一个数组为空，最后把另一个数组的剩余部分复制过来即可。
- 递归分解
    - 将数组分解成left和right，如果这两个数组内部数据是有序的，那么就可以用上面合并数组的方法将这两个数组合并排序
    - 重复上述分解过程，直至分解出的小组只含有一个元素时为止，此时认为该小组内部已有序。然后合并排序相邻二个小组即可。

###源码(python):
```
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
        if left[l] < right[r]:
            res.append(left[l])
            l += 1
        else:
            res.append(right[r])
            r += 1
    res += left[l:]
    res += right[r:]
    return res
```

##六. 快速排序 QuickSort

快速排序通常明显比同为Ο(n log n)的其他算法更快，因此常被采用，而且快排采用了分治法的思想，所以在很多笔试面试中能经常看到快排的影子。可见掌握快排的重要性.

###步骤:
- 从数列中挑出一个元素作为基准数
- 分区过程，将比基准数大的放到右边，小于或等于它的数都放到左边
- 再对左右区间递归执行第二步，直至各区间只有一个数

###源码(python):
```
def quicksort(arr, left, right):
    # 只有left < right 排序
    if left < right:
        pivot_index = partition(arr, left, right)
        quicksort(arr, left, pivot_index - 1)
        quicksort(arr, pivot_index + 1, right)


def partition(arr, left, right):
    """找到基准位置, 并返回"""
    pivot_index = left
    pivot = arr[left]

    for i in range(left + 1, right + 1):
        if arr[i] < pivot:
            # 如果此处索引的值小于基准值, 基准值的位置后移一位
            # 并将后移一位的值和这个值交换, 让基准位置及之前的始终小于基准值
            pivot_index += 1
            if pivot_index != i:
                arr[pivot_index], arr[i] = arr[i], arr[pivot_index]

    # 将基准值移动到正确的位置
    arr[left], arr[pivot_index] = arr[pivot_index], arr[left]

    return pivot_index
```

##七. 堆排序 HeapSort

堆排序在 top K 问题中使用比较频繁。堆排序是采用二叉堆的数据结构来实现的，虽然实质上还是一维数组。二叉堆是一个近似完全二叉树 。

###二叉堆具有以下性质：
- 父节点的键值总是大于或等于（小于或等于）任何一个子节点的键值
- 每个节点的左右子树都是一个二叉堆（都是最大堆或最小堆）

###步骤:
- 构造最大堆（Build_Max_Heap）：若数组下标范围为0~n，考虑到单独一个元素是大根堆，则从下标n/2开始的元素均为大根堆。于是只要从n/2-1开始，向前依次构造大根堆，这样就能保证，构造到某个节点时，它的左右子树都已经是大根堆。
- 堆排序（HeapSort）：由于堆是用数组模拟的。得到一个大根堆后，数组内部并不是有序的。因此需要将堆化数组有序化。思想是移除根节点，并做最大堆调整的递归运算。第一次将heap[0]与heap[n-1]交换，再对heap[0...n-2]做最大堆调整。第二次将heap[0]与heap[n-2]交换，再对heap[0...n-3]做最大堆调整。重复该操作直至heap[0]和heap[1]交换。由于每次都是将最大的数并入到后面的有序区间，故操作完后整个数组就是有序的了。
- 最大堆调整（Max_Heapify）：该方法是提供给上述两个过程调用的。目的是将堆的末端子节点作调整，使得子节点永远小于父节点

###源码(python):
```
def heap_sort(ary):
    n = len(ary)
    first = int(n / 2 - 1)  # 最后一个非叶子节点
    for start in range(first, -1, -1):  # 构造大根堆
        max_heapify(ary, start, n - 1)
    for end in range(n - 1, 0, -1):  # 堆排，将大根堆转换成有序数组
        ary[end], ary[0] = ary[0], ary[end]
        max_heapify(ary, 0, end - 1)
    return ary
# 最大堆调整：将堆的末端子节点作调整，使得子节点永远小于父节点
# start为当前需要调整最大堆的位置，end为调整边界


def max_heapify(ary, start, end):
    root = start
    while True:
        child = root * 2 + 1  # 调整节点的子节点
        if child > end:
            break
        if child + 1 <= end and ary[child] < ary[child + 1]:
            child = child + 1  # 取较大的子节点
        if ary[root] < ary[child]:  # 较大的子节点成为父节点
            ary[root], ary[child] = ary[child], ary[root]  # 交换
            root = child
        else:
            break
```

##八. 总结

**算法稳定性**:：假定在待排序的记录序列中，存在多个具有相同的关键字的记录，若经过排序，这些记录的相对次序保持不变，即在原序列中，ri=rj，且ri在rj之前，而在排序后的序列中，ri仍在rj之前，则称这种排序算法是稳定的；否则称为不稳定的.

**算法稳定性的重要性**:
- 在实际的应用中，我们交换的不一定只是一个整数，而可能是一个很大的对象，交换元素存在一定的开销

###算法的比较:

![算法的比较](https://github.com/mengyuwei290/Leecode/tree/master/Sorting/images/排序算法比较.png)
