class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_lenth = 0
        count = 0
        table = {0: 0}

        for index, num in enumerate(nums, 1):
            if num == 0:
                count -= 1
            if num == 1:
                count += 1

            if count in table:
                max_lenth = max(max_lenth, index - table[count])
            else:
                table[count] = index
        return max_lenth
