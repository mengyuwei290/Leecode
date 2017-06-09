依托于3Sum，目前只知道还是使用之前的方法，时间复杂度为O(n^3)，空间复杂度O(1)，感觉并没什么用处。

**注意**：
- “len(nums) < N or N < 2 or target < nums[0] * N or target > nums[-1] * N:”
可以一定的缩短时间。
- 开始前必须要sort一下
