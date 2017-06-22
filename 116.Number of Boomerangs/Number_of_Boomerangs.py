class Solution(object):
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        res = 0
        for p in points:
            dis = {}
            for q in points:
                s, f = (p[0] - q[0])**2, (p[1] - q[1])**2
                dis[s + f] = dis.get(s + f, 0) + 1
            for k in dis:
                res += dis[k] * (dis[k] - 1)
        return res
