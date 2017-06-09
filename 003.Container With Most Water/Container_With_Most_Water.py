class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        level, size, low, high = 0, 0, 0, len(height) - 1
        res = 0
        while low < high:
            if height[low] < height[high]:
                res = max(res, (high - low) * height[low])
                low += 1
            else:
                level = height[high]
                res = max(res, (high - low) * height[high])
                high -= 1
        return res


if __name__ == '__main__':
    ff = Solution()
    print(ff.maxArea([4, 2, 2, 5]))
