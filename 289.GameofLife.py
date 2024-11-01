class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
        Output: [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]
        由于新的0和1会影响后续遍历，因此用其他标记来代替0和1，从而去除干扰
        1 -> 0 -> 3
        0 -> 1 -> 2
        """
        newDict = {0:set([0,2]), 1: set([1,3])}
        def countNum(idx, jdx, flag):
            count = 0
            if idx - 1 >= 0 and jdx - 1 >= 0:
                if board[idx-1][jdx-1] in newDict[flag]:
                    count += 1
            if idx - 1 >= 0:
                if board[idx-1][jdx] in newDict[flag]:
                    count += 1
            if idx - 1 >= 0 and jdx + 1 < len(board[0]):
                if board[idx-1][jdx + 1] in newDict[flag]:
                    count += 1
            if jdx - 1 >= 0:
                if board[idx][jdx - 1] in newDict[flag]:
                    count += 1
            if jdx + 1 < len(board[0]):
                if board[idx][jdx + 1] in newDict[flag]:
                    count += 1
            if idx + 1 < len(board) and jdx - 1 >= 0:
                if board[idx + 1][jdx - 1] in newDict[flag]:
                    count += 1
            if idx + 1 < len(board):
                if board[idx + 1][jdx] in newDict[flag]:
                    count += 1
            if idx + 1 < len(board) and jdx + 1 < len(board[0]):
                if board[idx + 1][jdx + 1] in newDict[flag]:
                    count += 1
            return count
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                # 4 rules
                liveNeig = countNum(i, j, 1)
                if board[i][j] == 1:
                    
                    if liveNeig < 2:
                        # rule 1: 1 -> 0 -> 3
                        board[i][j] = 3
                    elif liveNeig > 3:
                        # rule 3: 1 -> 0 -> 3
                        board[i][j] = 3
                else:
                    if liveNeig == 3:
                        # rule 4: 0 -> 1 -> 2
                        board[i][j] = 2
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 2:
                    board[i][j] = 1
                elif board[i][j] == 3:
                    board[i][j] = 0
        return board

s = Solution()
res = s.gameOfLife([[0,1,0],[0,0,1],[1,1,1],[0,0,0]])
print(res)

                    
        
        