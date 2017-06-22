class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if len(s) < len(t):
            s, t = t, s
        a, b = map(collections.Counter, (s, t))
        return list((a - b).elements())[0]
