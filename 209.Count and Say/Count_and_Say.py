class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n <= 0: return ''

        res = '1'
        for _ in range(n-1):
            j, temp = 0, ''
            while j < len(res):
                count, num = 0, res[j]
                while j < len(res) and res[j] == num: j += 1; count += 1
                temp += str(count) + num
            res = temp
        return res
