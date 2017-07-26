class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        d = collections.Counter(magazine)
        for i in ransomNote:
            if d.get(i, 0): d[i] -= 1
            else: return False
        return True
