class Solution(object):
    def arrayNesting(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # find the size of all the isolated circles
        visited = [False] * len(nums)
        max_count = 0
        for i, num in enumerate(nums):
            count = 0
            while not visited[i]:
                visited[i] = True
                count += 1
                i = nums[i]
            max_count = max(count, max_count)
        return max_count
