用的Two Pointers的思想，时间复杂度O(N)，空间复杂度O(1)。

**步骤**：
- 判断是否满足迭代条件，l < r
- 每次从左右两边找低的边界，然后低的边界向中间推进(l++ or r--)
- 当level小于当前最低边界时，更新level
- 更新water的量，water += level - low
