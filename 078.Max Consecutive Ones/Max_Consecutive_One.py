class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        size, ans = 0, 0
        for n in nums:
            if n == 1:
                size += 1
                ans = max(ans, size)
            else:
                size = 0
        return ans
