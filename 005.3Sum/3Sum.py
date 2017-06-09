class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res, length = [], len(nums)
        for i in range(0, length - 2):
            if i == 0 or i > 0 and nums[i] != nums[i - 1]:
                lo, hi, two_sum = i + 1, length - 1, 0 - nums[i]
                while lo < hi:
                    if nums[lo] + nums[hi] == two_sum:
                        res += [nums[i], nums[lo], nums[hi]],
                        while lo < hi and nums[lo] == nums[lo + 1]:
                            lo += 1
                        while lo < hi and nums[hi] == nums[hi - 1]:
                            hi -= 1
                        lo += 1
                        hi -= 1
                    elif nums[lo] + nums[hi] < two_sum:
                        lo += 1
                    else:
                        hi -= 1
        return res
