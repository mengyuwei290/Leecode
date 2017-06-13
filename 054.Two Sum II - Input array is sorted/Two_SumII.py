class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        lo, hi, res = 0, len(numbers) - 1, [None, None]
        while lo < hi:
            if numbers[lo] + numbers[hi] == target:
                res = [lo + 1, hi + 1]
                break
            elif numbers[lo] + numbers[hi] < target:
                lo += 1
            else:
                hi -= 1
        return res
