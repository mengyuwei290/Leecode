class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        sums, result, d = 0, 0, {0: 1}

        for i in range(len(nums)):
            sums += nums[i]
            if sums - k in d:
                result += d.get(sums - k)
            d[sums] = d.get(sums, 0) + 1
        return result
