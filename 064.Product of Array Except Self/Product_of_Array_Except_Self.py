class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        if n <= 0:
            return []

        left, right = [1] * n, [1] * n
        for i in range(1, len(nums)):
            left[i] = left[i - 1] * nums[i - 1]
        for j in range(len(nums) - 2, -1, -1):
            right[j] = right[j + 1] * nums[j + 1]
        return list(map(lambda x, y: x * y, left, right))
