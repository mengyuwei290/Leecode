class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        if not board and not board[0]:
            return False

        inner_list = [[] for i in range(9)]
        col_list = [[] for i in range(9)]

        for i, row in enumerate(board):
            row_list = []
            for j, col in enumerate(row):
                in_index, col_index = (i // 3) * 3 + (j // 3), j
                if col == '.':
                    continue
                elif col not in inner_list[in_index] and col not in col_list[col_index] and col not in row_list:
                    inner_list[in_index].append(col)
                    col_list[col_index].append(col)
                    row_list.append(col)
                else:
                    return False
        return True
