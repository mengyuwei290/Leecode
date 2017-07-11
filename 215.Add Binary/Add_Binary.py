class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        s = ""
        c, i, j = 0, len(a)-1, len(b)-1
        while i>=0 or j>=0 or c == 1:
            c += int(a[i]) if i >= 0 else 0
            c += int(b[j]) if j >= 0 else 0
            s = str(c&1) + s; c >>= 1
            i, j = i-1, j-1
        return s
