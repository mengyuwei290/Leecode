class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix or not matrix[0]:
            return 0
        m, n = len(matrix), len(matrix[0])

        left, right, h, res = [0] * n, [n] * n, [0] * n, 0

        for i in range(m):
            cur_left, cur_right = 0, n
            for j in range(n):
                if matrix[i][j] == '1':
                    h[j] += 1
                else:
                    h[j] = 0

            for j in range(n):
                if matrix[i][j] == '1':
                    left[j] = max(left[j], cur_left)
                else:
                    left[j], cur_left = 0, j + 1

            for j in range(n - 1, -1, -1):
                if matrix[i][j] == '1':
                    right[j] = min(right[j], cur_right)
                else:
                    right[j], cur_right = n, j

            for j in range(n):
                res = max(res, (right[j] - left[j]) * h[j])
        return res
