class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for i in range(9):
            row = [item for item in board[i] if item != '.']
            if len(row) != len(set(row)):
                return False
        for i in range(9):
            col = [board[r][i] for r in range(9) if board[r][i] != '.']
            if len(col) != len(set(col)):
                return False
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                box = board[i][j:j + 3] + \
                    board[i+1][j:j + 3] + board[i+2][j:j + 3]
                box = [item for item in box if item != '.']
                if len(box) != len(set(box)):
                    return False
        return True
