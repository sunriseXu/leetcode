class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        # right: col + 1, [0, 1]
        # down: row + 1
        # left: col - 1
        # up: row - 1
        
        visited = set()
        initial = 0
        row = len(matrix)
        col = len(matrix[0])
        size = row * col
        visited.add((0,0))
        
        res = []
        res.append(matrix[0][0])
        currx, curry = 0, 0
        while len(visited) < size:
            tmpx = currx
            tmpy = curry
            if initial == 0:
                tmpy += 1
            elif initial == 1:
                tmpx += 1
            elif initial == 2:
                tmpy -= 1
            else:
                tmpx -= 1
            
            if tmpx >= row or tmpx < 0 or tmpy >= col or tmpy < 0 or (tmpx, tmpy) in visited:
                initial = (initial + 1) % 4
            else:
                currx = tmpx
                curry = tmpy
                visited.add((currx, curry))
                res.append(matrix[currx][curry])
        return res
            
        
        
sol = Solution()
res = sol.spiralOrder([[1,2,3],[4,5,6],[7,8,9]])
print(res)
        