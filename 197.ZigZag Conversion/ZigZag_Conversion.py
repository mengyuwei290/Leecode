class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        length = len(s)
        res = ['' for _ in range(numRows)]

        i = 0
        while i < length:
            idx = 0
            while idx < numRows and i < length:
                res[idx] += s[i]
                i += 1; idx += 1
            idx = numRows-2
            while idx >= 1 and i < length:
                res[idx] += s[i]
                i += 1; idx -= 1
        return ''.join(res)
