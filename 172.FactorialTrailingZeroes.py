class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        5! = 120 -> 1
        15 -> 5 10 15
        20 -> 5 10 15 20 25 30 35 40
        30 -> 5 10 15 20 25 30
              5 5  5  5  5 5 5
        """
        c = 0
        ori = n
        while ori > 0:
            n = ori - ori % 5
            while n % 5 == 0 and n > 0:
                n = n // 5
                c += 1
            ori -= 5
        return c
sol = Solution()
res = sol.trailingZeroes(3)
print(res)