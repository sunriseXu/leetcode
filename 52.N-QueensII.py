class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        matrix = []
        for i in range(n):
            matrix.append([0] * n)
            
        result = [0]
        def checkValid(i, j):
            # check rows
            for jj in range(0, j):
                if matrix[i][jj] == 1:
                    return False
            # check corner
            for ii, jj in zip(range(i - 1, -1, -1), range(j - 1, -1, -1)):
                if matrix[ii][jj] == 1:
                    return False
            # check corner
            for ii, jj in zip(range(i + 1, n, 1), range(j - 1, -1, -1)):
                if matrix[ii][jj] == 1:
                    return False
            return True
        
        def recursive(col):
            if col == n:
                result[0] += 1
                return True
            for row in range(n):
                if checkValid(row, col):
                    matrix[row][col] = 1
                    res = recursive(col + 1)
                    matrix[row][col] = 0
            return False
        recursive(0)
        return result[0]
s = Solution()
res = s.totalNQueens(5)
print(res)
        