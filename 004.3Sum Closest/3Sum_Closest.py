class Solution(object):
    def threeSumClosest(self, nums, target):
    """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
    if len(nums) < 3:
        return
    nums.sort()
    res = nums[0] + nums[1] + nums[2]
    for i in range(len(nums) - 2):
        lo, hi = i + 1, len(nums) - 1
        if i == 0 or (i > 0 and nums[i] != nums[i - 1]):
            while lo < hi:
                sums = nums[i] + nums[lo] + nums[hi]
                if sums == target:
                    return target
                if abs(sums - target) < abs(res - target):
                    res = sums
                if sums > target:
                    hi -= 1
                else:
                    lo += 1
    return res
