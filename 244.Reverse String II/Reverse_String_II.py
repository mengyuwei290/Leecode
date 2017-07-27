class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        if k == 0: return s
        if k >= len(s): return s[::-1]

        flag = -1
        len_irr = len(s)//k
        res = []
        for i in range(len_irr):
            sub = s[i*k:i*k+k:]
            res.append(sub[::flag])
            flag *= -1

        if k*len_irr < len(s):
            sub = s[k*len_irr:]
            res.append(sub[::flag])
        s = ''.join(res)
        return s
