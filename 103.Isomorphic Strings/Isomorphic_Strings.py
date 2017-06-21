class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return [s.find(i) for i in s] == [t.find(j) for j in t]

    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        m1, m2 = collections.defaultdict(int), collections.defaultdict(int)
        for i in range(len(s)):
            if m1[s[i]] != m2[t[i]]:
                return False
            m1[s[i]] = i + 1
            m2[t[i]] = i + 1
        return True
