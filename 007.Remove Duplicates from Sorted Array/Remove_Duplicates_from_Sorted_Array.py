class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        size = 0
        for i in range(nums):
            if i == 0 or (i > 0 and nums[i] != nums[i - 1]):
                nums[i] = nums[size]
                size += 1
        return size
