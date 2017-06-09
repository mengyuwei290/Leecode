class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums) - 1, 0, -1):
            if nums[i] > nums[i - 1]:
                index = i
                for j in range(len(nums) - 1, i - 1, -1):
                    if nums[j] > nums[i - 1]:
                        index = j
                        break
                nums[index], nums[i - 1] = nums[i - 1], nums[index]
                for j in range(i, (i + len(nums)) // 2):
                    nums[j], nums[len(nums) - 1 - j + i] = nums[len(nums) - 1 - j + i], nums[j]
                break
        else:
            nums.reverse()
