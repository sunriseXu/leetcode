class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        '''
        dp[i] = d[i] + dp2[i-1]
        '''
        
        # init first row 
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [0] * n
        if obstacleGrid[0][0] == 0:
            dp[0] = 1 
        for i in range(1, n):
            if obstacleGrid[0][i] == 0 and dp[i-1] > 0:
                dp[i] = dp[i-1]
        for i in range(1, m):
            dp2 = [0] * n
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    dp2[j] = 0
                else:
                    if j-1 < 0:
                        dp2[j] = dp[j]
                    else:
                        dp2[j] = dp[j] + dp2[j-1]
            dp = dp2
        return dp[-1]
s = Solution()
res = s.uniquePathsWithObstacles([[1]])
print(res)
                