class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if len(s) < 10:
            return []

        seen, res = set(), set()
        for i in range(len(s) - 9):
            str1 = s[i:i + 10]
            if str1 not in seen:
                seen.add(str1)
            else:
                res.add(str1)
        return list(res)
