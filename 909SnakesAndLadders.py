# You are given an n x n integer matrix board where the cells are labeled from 1 to n2 in a Boustrophedon style starting from the bottom left of the board (i.e. board[n - 1][0]) and alternating direction each row.

# You start on square 1 of the board. In each move, starting from square curr, do the following:

# Choose a destination square next with a label in the range [curr + 1, min(curr + 6, n2)].
# This choice simulates the result of a standard 6-sided die roll: i.e., there are always at most 6 destinations, regardless of the size of the board.
# If next has a snake or ladder, you must move to the destination of that snake or ladder. Otherwise, you move to next.
# The game ends when you reach the square n2.
# A board square on row r and column c has a snake or ladder if board[r][c] != -1. The destination of that snake or ladder is board[r][c]. Squares 1 and n2 do not have a snake or ladder.

# Note that you only take a snake or ladder at most once per move. If the destination to a snake or ladder is the start of another snake or ladder, you do not follow the subsequent snake or ladder.

# For example, suppose the board is [[-1,4],[-1,3]], and on the first move, your destination square is 2. You follow the ladder to square 3, but do not follow the subsequent ladder to 4.
# Return the least number of moves required to reach the square n2. If it is not possible to reach the square, return -1.
class Solution(object):
    def snakesAndLadders(self, board):
        """
        https://www.nileshblog.tech/leetcode-solving-snakes-and-ladders-with-bfs-algorithm/
        :type board: List[List[int]]
        :rtype: int
        """        
        
        queue = []
        visited = set()
        
        row = len(board)
        maxLabel = row * row
        dist = [float('inf')] * (maxLabel + 1)
        dist[1] = 0
        
        queue.append(1)
        visited.add(1)
                
        while queue:
            curr = queue.pop(0)
            if curr == maxLabel:
                return dist[curr]
            for i in range(1, 7):
                nnext = curr + i
                if nnext > maxLabel or nnext in visited:
                    continue
                nrow, ncol = self.labelToCord(nnext, row)
                if board[nrow][ncol] != -1:
                    visited.add(nnext)
                    nnext = board[nrow][ncol]
                if nnext not in visited:
                    queue.append(nnext)
                    visited.add(nnext)
                    dist[nnext] = min(dist[curr] + 1, dist[nnext])
        return -1 
    def labelToCord(self, label, size):
        row = float(label) / size # 2
        tmp = int(label / size) # 2
        if tmp < row:
            row = tmp + 1
        else:
            row = tmp
        col = (label - 1) % size
        if row % 2 == 0:
            col = size - col - 1
        return size - row, col
sol = Solution()
res = sol.snakesAndLadders([[-1,-1,-1,46,47,-1,-1,-1],[51,-1,-1,63,-1,31,21,-1],[-1,-1,26,-1,-1,38,-1,-1],[-1,-1,11,-1,14,23,56,57],[11,-1,-1,-1,49,36,-1,48],[-1,-1,-1,33,56,-1,57,21],[-1,-1,-1,-1,-1,-1,2,-1],[-1,-1,-1,8,3,-1,6,56]])
print(res)       