class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res self.target = [], target
        candidates.sort()
        self.combinationSum_helper(candidates, 0, 0, [], res)
        return res

    def combinationSum_helper(self, nums, idx, sums, path, res):
        if sums == self.target:
            res += path[:],
            return

        for i in range(idx, len(nums)):
            if sums + nums[i] <= self.target:
                path += nums[i],
                self.combinationSum_helper(nums, i, sums + nums[i], path, res)
                path.pop()
