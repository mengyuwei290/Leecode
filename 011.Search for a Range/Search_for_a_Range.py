class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if nums[mid] == target:
                start, end = mid, mid
                while start >= 0 and nums[start] == nums[mid]:
                    start -= 1
                while end < len(nums) and nums[end] == nums[mid]:
                    end += 1
                return [start + 1, end - 1]
            elif nums[mid] > target:
                hi = mid - 1
            else:
                lo = mid + 1
        return [-1, -1]
