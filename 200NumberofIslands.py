# Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

 

# Example 1:

# Input: grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]
# Output: 1

class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        rowSize = len(grid)
        colSize = len(grid[0])
        move = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        visited = set()
        count = 0
        def helper(startx, starty):
            # up y--
            # down y++
            # left x--
            # right x++
            queue = []
            queue.append((startx, starty))
            visited.add((startx, starty))
            while queue:
                curr = queue.pop(0)
                currx = curr[0]
                curry = curr[1]
                for step in move:
                    newx = currx + step[0]
                    newy = curry + step[1]
                    if (newx, newy) not in visited and newx > -1 and newx < rowSize and newy > -1 and newy < colSize and grid[newx][newy] == '1':
                        queue.append((newx, newy))  
                        visited.add((newx, newy)) 
        for i in range(rowSize):
            for j in range(colSize):
                if grid[i][j] == '1' and (i, j) not in visited:
                    helper(i, j)
                    count += 1
        return count
sol = Solution()
res = sol.numIslands(grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
])
print(res)
        