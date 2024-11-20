class Solution(object):
    def climbStairs(self, n):
        if n == 1:
            return 1
        if n == 2:
            return 2
        last = 1
        current = 2
        for i in range(n-2):
            tmp = current
            current += last
            last = tmp
        return current
s = Solution()
res = s.climbStairs(6)
print(res)