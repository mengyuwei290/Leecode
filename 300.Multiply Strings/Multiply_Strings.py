class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        m, n = len(num1), len(num2)
        pos = [0]*(m+n)

        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                mul = int(num1[i]) * int(num2[j])
                p1, p2 = i+j, i+j+1
                ans = mul + pos[p2]
                pos[p1] += ans/10; pos[p2] = ans%10
        s = []
        for p in pos:
            if len(s) == 0 and p == 0: continue
            s += str(p),
        return '0' if len(s) == 0 else ''.join(s)
