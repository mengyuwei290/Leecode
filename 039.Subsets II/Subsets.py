class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = [[]]
        nums.sort()
        for n in nums:
            res += [i + [n] for i in res if i + [n] not in res]
        return res
