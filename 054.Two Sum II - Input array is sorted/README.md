简单就是一个Two Pointers, 有序的更好处理, 就像在3Sum里那样, 我们先会对数组进行排序.而对于之前的Two Sum, 由于sort的时间复杂度是O(NlogN), 所以没有必要取做sort, 因为本身的Two Pointers就是O(N)的算法.
