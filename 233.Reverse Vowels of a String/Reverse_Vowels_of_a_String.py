class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        t = 'aeiouAEIOU'
        l, r = 0, len(s)-1
        s = list(s)
        while l < r:
            while l < r and s[l] not in t: l += 1
            while l < r and s[r] not in t: r -= 1
            while l < r: s[l], s[r] = s[r], s[l]
            l += 1; r -= 1
        return ''.join(s)
