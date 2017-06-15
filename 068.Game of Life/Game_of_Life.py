class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return

        m, n = len(board), len(board[0])

        def count_nums(x, y):
            d = 0
            row = [x + i for i in range(-1, 2, 1) if x + i < m and x + i >= 0]
            col = [y + j for j in range(-1, 2, 1) if y + j < n and y + j >= 0]
            for i in row:
                for j in col:
                    if not i == x or not j == y:
                        if board[i][j] & 1:
                            d += 1
            return d

        for i in range(m):
            for j in range(n):
                d = count_nums(i, j)
                if board[i][j] == 1:
                    if d == 2 or d == 3:
                        board[i][j] = 3
                else:
                    if d == 3:
                        board[i][j] = 2
        for i in range(m):
            for j in range(n):
                board[i][j] >>= 1
