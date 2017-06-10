class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        water, l, r, level = 0, 0, len(height) - 1, 0
        while l < r:
            if height[l] <= height[r]:
                low = height[l]
                l += 1
            else:
                low = height[r]
                r -= 1
            if low > level:
                level = low
            water += level - low
        return water
