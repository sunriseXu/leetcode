class Solution(object):
    def setZeroes(self, matrix):
        # set indicators for first row and column
        first_row = 0 in matrix[0]
        first_column = any(i[0]==0 for i in matrix)
        m = len(matrix)
        n = len(matrix[0])

        # set row and column indicators to zero
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        # set inner matrix values to zero
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        # set first row to zero if neccessary
        if first_row:
            matrix[0] = [0] * n
        if first_column:
            for i in range(0, m):
                matrix[i][0] = 0
        return matrix

s = Solution()
res = s.setZeroes([[1,1,1],[1,0,1],[1,1,1]])
print(res)