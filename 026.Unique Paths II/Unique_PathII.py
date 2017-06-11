class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if not obstacleGrid or not obstacleGrid[0] or obstacleGrid[0][0]:
            return 0

        m, n = len(obstacleGrid), len(obstacleGrid[0])

        aux = [[1 for x in range(n)] for x in range(m)]
        for i in range(1, m):
            if obstacleGrid[i][0] == 1:
                aux[i][0] = 0
                continue
            aux[i][0] = aux[i - 1][0]
        for j in range(1, n):
            if obstacleGrid[0][j] == 1:
                aux[0][j] = 0
                continue
            aux[0][j] = aux[0][j - 1]

        for i in range(1, m):
            for j in range(1, n):
                aux[i][j] = aux[i][j - 1] + aux[i - 1][j]
                if obstacleGrid[i][j] == 1:
                    aux[i][j] = 0
        return aux[-1][-1]
