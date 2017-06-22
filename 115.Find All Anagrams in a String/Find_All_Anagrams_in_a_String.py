class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        res = []
        n, m = len(s), len(p)
        if n < m:
            return res

        phash, shash = [0] * 123, [0] * 123
        for i in p:
            phash[ord(i)] += 1
        for i in s[:m - 1]:
            shash[ord(i)] += 1

        for i in range(m - 1, n):
            shash[ord(s[i])] += 1
            if shash == phash:
                res.append(i - m + 1)
            shash[ord(s[i - m + 1])] -= 1
        return res
