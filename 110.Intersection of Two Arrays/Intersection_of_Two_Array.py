class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """

        num1, num2 = set(nums1), set(nums2)
        return [i for i in num1 & num2]
