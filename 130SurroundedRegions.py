# Given an m x n matrix board containing 'X' and 'O', capture all regions that are 4-directionally surrounded by 'X'.

# A region is captured by flipping all 'O's into 'X's in that surrounded region.

# [["X","X","X","X"],
#  ["X","O","O","X"],
#  ["X","X","O","X"],
#  ["X","O","X","X"]]


# [["X","X","X","X"],
#  ["X","X","X","X"],
#  ["X","X","X","X"],
#  ["X","O","X","X"]]


[["X","X","X"],
 ["X","O","X"],
 ["X","X","X"]]
 
class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        visited = set()
        movement = [(0, -1), (0, 1), (1, 0), (-1, 0)]
        rowSize = len(board)
        colSize = len(board[0])
        def helper(startx, starty):
            queue = []
            currentVisited = set()
            queue.append((startx, starty))
            currentVisited.add((startx, starty))
            flag = True
            while queue:
                curr = queue.pop(0)
                for step in movement:
                    newx = curr[0] + step[0]
                    newy = curr[1] + step[1]
                    if newx == -1 or newx == rowSize or newy == -1 or newy == colSize:
                        flag = False
                    else:
                        if board[newx][newy] == 'O' and (newx, newy) not in currentVisited:
                            currentVisited.add((newx, newy))
                            visited.add((newx, newy))
                            queue.append((newx, newy))
            if flag:
                # surrounded by 'o'
                for cell in currentVisited:
                    board[cell[0]][cell[1]] = 'X'
            
        for i in range(rowSize):
            for j in range(colSize):
                if (i,j) not in visited and board[i][j] == 'O':
                    helper(i, j)
        return board

sol = Solution()
res = sol.solve([["X","X","X"],
 ["X","O","X"],
 ["X","X","X"]])
print(res)