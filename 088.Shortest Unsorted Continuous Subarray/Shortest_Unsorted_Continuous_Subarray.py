class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n, beg, end, Min, Max = len(nums), -1, -2, nums[-1], nums[0]
        for i in range(1, n):
            Max, Min = max(Max, nums[i]), min(Min, nums[n - 1 - i])
            if nums[i] < Max:
                end = i
            if nums[n - 1 - i] > Min:
                beg = n - 1 - i
        return end - beg + 1
