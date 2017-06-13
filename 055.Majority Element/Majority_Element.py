class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res, cnt = nums[0], 1
        for n in nums[1:]:
            if cnt == 0:
                res = n
            if n == res:
                cnt += 1
            else:
                cnt -= 1
        return res
