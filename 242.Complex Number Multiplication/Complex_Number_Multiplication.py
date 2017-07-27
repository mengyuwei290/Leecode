class Solution(object):
    def complexNumberMultiply(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        num1, num2 = [], []
        for s in a.split('+'):
            if s[-1] == 'i': num1 += int(s[:-1]),
            else: num1 += int(s),
        for s in b.split('+'):
            if s[-1] == 'i': num2 += int(s[:-1]),
            else: num2 += int(s),
        res = [num1[0]*num2[0]-num1[1]*num2[1], num1[0]*num2[1]+num1[1]*num2[0]]
        return str(res[0])+'+'+str(res[1])+'i'
        
