class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        version1 = map(int, version1.split('.'))
        version2 = map(int, version2.split('.'))
        length = min(len(version1), len(version2))
        for i in range(length):
            if version1[i] > version2[i]:
                return 1
            elif version1[i] < version2[i]:
                return -1
        else:
            if length < len(version1) and version1[-1] > 0:
                return 1
            elif length < len(version2) and version2[-1] > 0:
                return -1
            else: return 0
