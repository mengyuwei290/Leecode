class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ans = []
        self.backtrack(ans, '', 0, 0, n)
        return ans
    def backtrack(self, res, s, left, right, n):
        if len(s) == 2*n:
            res.append(s)
            return

        if left < n: self.backtrack(res, s+'(', left+1, right, n)
        if right < left: self.backtrack(res, s+')', left, right+1, n)
