class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(0, n // 2):
            for j in range(i, n - i - 1):
                temp = matrix[i][j]
                matrix[i][j], matrix[n - j - 1][i], matrix[n - i - 1][n - j - 1], matrix[j][n - i - 1] = \
                    matrix[n - j - 1][i], matrix[n - i - 1][n - j - 1], matrix[j][n - i - 1], temp
