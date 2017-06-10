class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sums, res = 0, nums[0]
        for i in nums:
            sums = i + sums if sums >= 0 else i
            res = max(res, sums)
        return res
