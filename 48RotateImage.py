class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        
        """
        # 1 2 3 4
        # 4 5 6 4
        # 7 8 9 4
        # 4 4 4 4
        # (0, 0) = (2, 0) (0, 2) = (0, 0) (2, 2) = (0, 2) (2, 0) = (2, 2)
        n = len(matrix)
        x = n // 2
        y = n - x
        for i in range(x):
            for j in range(y):
                matrix[i][j], matrix[j][~i], matrix[~i][~j], matrix[~j][i] = \
                    matrix[~j][i], matrix[i][j], matrix[j][~i], matrix[~i][~j]
        return matrix

sol = Solution()
res = sol.rotate([[0, 1], [2, 3]])
print(res)
        