class Solution(object):
    def findLUSlength(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        c = collections.Counter(strs)
        def isSub(s1, s2):
            it = iter(s1)
            return len(s1) >= len(s2) and all(i in it for i in s2)
        for s2 in sorted([str for str in c if c[str] == 1], key=len, reverse=True):
            if sum(map(lambda s1: isSub(s1, s2), strs)) == 1:
                return len(s2)
        return -1
