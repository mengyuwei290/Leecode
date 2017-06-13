class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ll = [float('-inf')] + nums[:] + [float('-inf')]
        m = len(nums)
        for i in range(1, m + 1):
            if ll[i] > ll[i - 1] and ll[i] > ll[i + 1]:
                return i - 1
        return
