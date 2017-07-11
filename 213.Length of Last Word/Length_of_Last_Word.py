class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = s.split(' ')
        while l and l[-1] == '':
            l.pop()
        return 0 if not l else len(l[-1])
