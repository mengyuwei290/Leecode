class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sets = set(nums)
        best = 0
        for i in nums:
            x = i
            if x - 1 not in sets:
                y = x + 1
                while y in sets:
                    y += 1
                best = max(best, y - x)
        return best
