class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        ans = 0
        flag = 0
        d = collections.Counter(s)
        for k, v in d.items():
            if v % 2 == 0:
                ans += v
            else:
                ans += v - 1
                flag = 1
        return ans if flag == 0 else ans + 1
