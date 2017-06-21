class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False

        dic1, dic2 = [0] * 26, [0] * 26
        for i in range(len(s)):
            dic1[ord(s[i]) - ord('a')] += 1
            dic2[ord(t[i]) - ord('a')] += 1
        return dic1 == dic2
