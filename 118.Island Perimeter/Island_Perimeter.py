class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        return sum(sum(map(operator.ne, [0] + row, row + [0]))
                   for row in grid + list(map(list, zip(*grid))))
