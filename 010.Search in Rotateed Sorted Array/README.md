典型的二分查找的方法，由于二分查找利用了数组的有序性，所以时间复杂度为O(logN)，空间复杂的为O(1)。

利用nums[mid]的值与nums[l]的值进行比较，确定当前mid是在前半部分还是后半部分，然后再根据target值的大小确定lo或hi的变化。