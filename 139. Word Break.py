class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
        """
        results = dict()
        def findPrefix(substring):
            res = []
            for i in wordDict:
                if substring.startswith(i):
                    res.append(i)
            return res
        def recurse(substring):
            if substring in results:
                return False
            if substring == '':
                return True
            prefixs = findPrefix(substring)
            if not prefixs:
                results[substring] = False
                return False
            for prefix in prefixs:
                if recurse(substring[len(prefix):]):
                    return True
            results[substring] = False
            return False
        return recurse(s)
s = Solution()
res = s.wordBreak(s = "catsandog", wordDict = ["cats","dog","sand","and","cat"])
print(res)