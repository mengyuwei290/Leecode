时间复杂度是O(N^2), 空间复杂度是O(N).

对每一个点计算与之对应的各个点的距离, 用它来当做key来计数, 最后输出 nums * (nums - 1)
