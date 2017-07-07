class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        tables = [[False] *(len(s) + 1) for _ in range(len(p) + 1)]

        tables[0][0] = True
        # fix the conner
        for i in range(2, len(p) + 1):
            tables[i][0] = tables[i-2][0] and p[i-1] == '*'

        for i in range(1, len(p) + 1):
            for j in range(1, len(s) + 1):
                if p[i-1] != '*':
                    tables[i][j] = tables[i-1][j-1] and (p[i-1] == s[j-1] or p[i-1] == ".")
                else:
                    tables[i][j] = tables[i-2][j] or tables[i-1][j]
                    if p[i-2] == s[j-1] or p[i-2] == '.': tables[i][j] |= tables[i][j-1]
        return tables[-1][-1]
