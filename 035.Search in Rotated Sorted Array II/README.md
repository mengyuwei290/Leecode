和上一题唯一不同的时, 数组有了重复的元素, 我们在上一题的基础上, 加了:
```
while l < mid and nums[l] == nums[mid]:
    l += 1
```
这使得nums[l]和nums[mid]的值尽量不相等(当mid前的值都是相同值时, mid == l, target不可能在mid的前半部分), 即可以确定mid时在rotated后的前半部分还是后半部分.
