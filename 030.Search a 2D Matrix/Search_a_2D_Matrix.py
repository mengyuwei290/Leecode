class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False

        i, j, m, n = 0, 0, len(matrix), len(matrix[0])
        while i < m - 1 and matrix[i][-1] < target:
            i += 1
        while j < n and matrix[i][j] < target:
            j += 1
        return False if j == n or matrix[i][j] != target else True
