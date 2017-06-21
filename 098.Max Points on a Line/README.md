时间复杂度是O(N^2), 空间复杂度是O(N^2)(最坏情况).

遍历所有两点的直线, 用字典来存储它们的斜率, 然后在每一次外层迭代后, 更新在一条线内点的最大数量.

**注意**:
- 对于任意两个点, 先求它们在x, y上的差dx,dy, 然后除去两者的最大公约数(因为正在的斜率时dy/dx)
- 注意dx和dy都为0的点, 这些点时重复点, 直接设置为重复点