class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        candidates.sort()
        self.dfs(candidates, target, 0, [], res)
        return res

    def combinationSum2_helper(self, nums, target, index, path, res):
        if target == 0:
            res.append(path)
            return
        for i in xrange(index, len(nums)):
            if i > index and nums[i] == nums[i - 1]:
                continue
            if target - nums[i] >= 0:
                path += nums[i],
                self.combinationSum2_helper(nums, target - nums[i], i + 1, path, res)
                path.pop()
