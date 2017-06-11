class Solution(object):
    def exist(self, board, word):
        if not board:
            return False
        r, c = len(board), len(board[0])
        visited = [[False for i in range(c)] for j in range(r)]
        for i in range(r):
            for j in range(c):
                if self.Word_Search_dfs(board, word, visited, i, j):
                    return True
        return False

    def Word_Search_dfs(self, board, word, visited, i, j):
        if not word:
            return True
        if i < 0 or i == len(board) or j < 0 or j == len(board[0]) \
                or visited[i][j] or word[0] != board[i][j]:
            return False
        visited[i][j] = True
        res = self.Word_Search_dfs(board, word[1:], visited, i + 1, j) or \
            self.Word_Search_dfs(board, word[1:], visited, i - 1, j) or \
            self.Word_Search_dfs(board, word[1:], visited, i, j - 1) or \
            self.Word_Search_dfs(board, word[1:], visited, i, j + 1)
        visited[i][j] = False
        return res
