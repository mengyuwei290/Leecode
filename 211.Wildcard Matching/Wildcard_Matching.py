class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        i, j, star, ss = 0, 0, None, 0
        while i < len(s):
            if  j < len(p) and (p[j] == '?' or s[i] == p[j]):
                i += 1; j += 1; continue
            if j < len(p) and p[j] == '*':
                star = j; j += 1; ss = i; continue
            if star != None:
                ss += 1
                j, i = star + 1, ss; continue
            return False
        while j < len(p) and p[j] == '*':
            j += 1
        return i >= len(s) and j >= len(p)
