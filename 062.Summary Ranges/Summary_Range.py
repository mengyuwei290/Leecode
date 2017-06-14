class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        ranges = []
        for n in nums:
            if not ranges or n > ranges[-1][-1] + 1:
                ranges += [],
            ranges[-1][1:] = n,
        return ['->'.join(map(str, r)) for r in ranges]


if __name__ == '__main__':
    nums = [0, 1, 3, 4, 7]
    ff = Solution()
    print(ff.summaryRanges(nums))
