class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        n = 3
        ["((()))","(()())","(())()","()(())","()()()"]
        """
        stack = []
        res = []
        def genItem(openN, closedN):
            if openN == closedN == n:
                res.append(''.join(stack))
                return
            if openN < n:
                stack.append('(')
                genItem(openN + 1, closedN)
                stack.pop()
            if closedN < openN:
                stack.append(')')
                genItem(openN, closedN + 1)
                stack.pop()
        genItem(0,0)
        return res

s = Solution()
res = s.generateParenthesis(3)
print(res)
        