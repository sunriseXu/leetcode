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
        dp = [i for i in triangle[-1]]
        for i in range(len(triangle) - 1):
            current = triangle[len(triangle) - i - 2]
            for j in range(len(current)):
                dp[j] = min(dp[j], dp[j+1]) + current[j]
        return dp[0]

s = Solution()
res = s.minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]])
print(res)