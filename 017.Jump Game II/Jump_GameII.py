class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return 0

        i, cur_max, cur_next, step = 0, nums[0], 0, 1

        while cur_max < len(nums) - 1:
            step += 1
            while i <= cur_max:
                if i + nums[i] > cur_next + nums[cur_next]:
                    cur_next = i
                i += 1
            cur_max = cur_next + nums[cur_next]
        return step
