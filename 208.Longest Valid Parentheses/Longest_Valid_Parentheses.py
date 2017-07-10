class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s: return 0

        longest = [0]*len(s)
        for i in range(1, len(s)):
            if s[i] == ')':
                if s[i-1] == '(':
                    longest[i] = longest[i-2] + 2 if i >= 2 else 2
                else:
                    if i - longest[i-1] -1 >= 0 and s[i - longest[i-1] -1] == '(':
                        longest[i] = longest[i-1] + 2 + \
                        (longest[i - longest[i-1] -2] if i - longest[i-1] -2 >=0 else 0)
        return max(longest)
