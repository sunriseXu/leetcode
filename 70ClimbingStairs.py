class Solution(object):
    def __init__(self):
        from collections import defaultdict
        self.map = defaultdict()
        self.map[1] = 1
        self.map[2] = 2
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n in self.map:
            return self.map[n]
        res = self.climbStairs(n-1) + self.climbStairs(n - 2)
        self.map[n] = res
        return res


sol = Solution()
res = sol.climbStairs(10)
print(res)