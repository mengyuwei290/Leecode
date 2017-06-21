class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not board or len(board) == 0:
            return
        self.solve(board)

    def solve(self, board):
        if self.full_board(board):
            return True
        idx = self.findindex(board)
        if idx:
            c_list = self.findAvaible(idx[2])
            for c in c_list:
                board[idx[0]][idx[1]] = c
                if self.solve(board):
                    return True
                else:
                    board[idx[0]][idx[1]] = '.'
            return False
        else:
            return False

    def findAvaible(self, m):
        i, res = 1, []
        while m:
            if m & 1:
                res += str(i),
            m >>= 1
            i += 1
        return res

    def findindex(self, board):
        res, r, c, g, result = None, [0] * 9, [0] * 9, [0] * 9, None
        mask = 0x1ff

        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    num = 1 << (ord(board[i][j]) - ord('1'))
                    r[i] |= num
                    c[j] |= num
                    g[i / 3 * 3 + j / 3] |= num
        for i in range(9):
            r[i] ^= mask
            c[i] ^= mask
            g[i] ^= mask
        min_dof = float('inf')
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    m = r[i] & c[j] & g[i / 3 * 3 + j / 3]
                    if m == 0:
                        return None
                    n = self.count_bit(m)
                    if n < min_dof:
                        min_dof = n
                        result = (i, j, m)
        return result

    def count_bit(self, x):
        ans = 0
        while x != 0:
            ans += 1 if x & 1 else 0
            x >>= 1
        return ans

    def full_board(self, board):
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    return False
        return True
