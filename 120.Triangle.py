class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
                2
               3 4
              6 5 7
             4 1 8 3
        
        """
        dp = [val for val in triangle[-1]]
        length = len(dp)
        for i in range(length - 2, -1, -1):
            for j in range(i + 1):
                dp[j] = triangle[i][j] + min(dp[j], dp[j+1])
        return dp[0]

sol = Solution()
res = sol.minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]])
print(res)
        