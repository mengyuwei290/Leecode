class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        size = 0
        for j in range(len(nums)):
            if size < 2 or nums[j] > nums[size - 2]:
                nums[size] = nums[j]
                size += 1
        return size
