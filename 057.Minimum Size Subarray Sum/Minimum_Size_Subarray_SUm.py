class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        i, j, res, min_value = 0, 0, 0, float('inf')
        while j < len(nums):
            res += nums[j]
            j += 1
            while res >= s:
                min_value = min(min_value, j - i)
                res -= nums[i]
                i += 1
        return 0 if min_value == float('inf') else min_value
