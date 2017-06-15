class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m1, m2, m3 = None, None, None

        for n in nums:
            if n == m1 or n == m2 or n == m3:
                continue
            if m1 == None or m1 < n:
                m1, m2, m3 = n, m1, m2
            elif m2 == None or m2 < n:
                m2, m3 = n, m2
            elif m3 == None or m3 < n:
                m3 = n
        return m3 if m3 != None else m1
