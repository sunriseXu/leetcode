# Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

# Each row must contain the digits 1-9 without repetition.
# Each column must contain the digits 1-9 without repetition.
# Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
# Note:

# A Sudoku board (partially filled) could be valid but is not necessarily solvable.
# Only the filled cells need to be validated according to the mentioned rules.
class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        # varify row
        def isUniq(input):
            uniq = set()
            for i in input:
                if i in uniq:
                    return False
                uniq.add(i)
            return True
        for i in range(0, 9):
            tmp = []
            for j in range(0, 9):
                if board[i][j] != '.':
                    tmp.append(board[i][j])
            if not isUniq(tmp):
                return False
        
        for i in range(0, 9):
            tmp = []
            for j in range(0, 9):
                if board[j][i] != '.':
                    tmp.append(board[j][i])
            if not isUniq(tmp):
                return False
        for i in range(0, 9):
            col = i % 3
            row = i // 3
            col *= 3
            row *= 3
            tmp = []
            for m in range(row, row + 3):
                for n in range(col, col + 3):
                    if board[m][n] != '.':
                        tmp.append(board[m][n])
            if not isUniq(tmp):
                return False
        return True
sol = Solution()
res = sol.isValidSudoku([["8","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]])
print(res)