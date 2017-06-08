class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) <= 1:
            return False
        mydict = {}
        for i in range(0, len(nums)):
            if nums[i] in mydict:
                return [mydict[nums[i]], i]
            else:
                mydict[target - nums[i]] = i


if __name__ == '__main__':
    ff = Solution()
    print(ff.twoSum([2, 7, 11, 15], 9))
