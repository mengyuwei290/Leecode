class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        s = pattern
        t = str.split()
        if len(t) != len(s):
            return False

        m1, m2 = collections.defaultdict(int), collections.defaultdict(int)
        for i in range(len(s)):
            if m1[s[i]] != m2[t[i]]:
                return False
            m1[s[i]] = i + 1
            m2[t[i]] = i + 1
        return True
