class Solution:
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        self.dfs(0, 0, board)

    def dfs(self, x, y, board):
        x, y = self.nextpos(x, y, board)
        if x == -1:
            return True
        for val in '123456789':
            if self.check(val, x, y, board):
                board[x][y] = val
                if self.dfs(x, y, board):
                    return True
                board[x][y] = '.'

    def nextpos(self, x, y, board):
        # 获取下一个空位置
        for j in range(y, 9):
            if board[x][j] == '.':
                return x, j
        for i in range(x + 1, 9):
            for j in range(9):
                if board[i][j] == '.':
                    return i, j
        return -1, -1

    def check(self, val, x, y, board):
        # 检查行
        if val in board[x]:
            return False
        # 检查列
        for i in range(9):
            if val == board[i][y]:
                return False
        # 检查九宫格
        m, n = x//3*3, y//3*3
        for i in range(3):
            if val in board[m+i][n:n+3]:
                return False
        return True
