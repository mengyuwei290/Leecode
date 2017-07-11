class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        try:
            a = float(s.strip())
            return True
        except:
            return False
