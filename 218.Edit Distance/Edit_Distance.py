class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        m, n = len(word1), len(word2)
        d = [[0]*(n+1) for _ in range(m+1)]
        for i in range(1, n+1): d[0][i] = i
        for i in range(1, m+1): d[i][0] = i

        for j in range(1, n+1):
            for i in range(1, m+1):
            # insert = d[i][j-1] + 1
            # delete = d[i-1][j] + 1
            # mismatch = d[i-1][j-1] + 1
            # match = d[i-1][j-1]
                if word1[i-1] == word2[j-1]:
                    d[i][j] = d[i-1][j-1]
                else:
                    d[i][j] = min(d[i][j-1], d[i-1][j], d[i-1][j-1]) + 1
        return d[-1][-1]
