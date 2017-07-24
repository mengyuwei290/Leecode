class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        def isValid(s):
            if len(s) > 3 and len(s) == 0 or (s[0] == '0' and len(s) > 1) or (int(s) > 255):
                return False
            return True
        length, res = len(s), []
        for i in range(1, min(4, length-2)):
            for j in range(i+1, min(i+4, length-1)):
                for k in range(j+1, min(j+4, length)):
                    s1=s[:i]; s2=s[i:j]; s3=s[j:k]; s4=s[k:]
                    if isValid(s1) and isValid(s2) and isValid(s3) and isValid(s4):
                        res += s1+'.'+s2+'.'+s3+'.'+s4,
        return res
