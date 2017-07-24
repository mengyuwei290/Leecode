class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s or s == '0' or s[0] == '0': return 0
        n = len(s)
        num = [0] * (n+1);
        num[0], num[1] = 1, 1

        for i in range(2, n+1):
            if int(s[i-2:i]) <= 26 and int(s[i-2:i]) > 9:
                num[i] += num[i-2]
            if s[i-1:i] != '0':
                num[i] += num[i-1]
        return num[-1]
