class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        self.dict= { '2':'abc', '3':'edf', '4':'ghi', '5':'jkl', '6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        res = []
        if digits == '':
            return res
        self.bfs(digits, 0, len(digits), '', res)
        return res
        
    def bfs(self, digits, curr, k, currChars, res):
        if curr == k:
            res.append(currChars)
            return
        chars = self.dict[digits[curr]]
        for i in chars:
            self.bfs(digits, curr + 1, k, currChars + i, res)

sol = Solution()
res = sol.letterCombinations("2")
print(res)