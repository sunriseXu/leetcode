class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
        """
        from collections import defaultdict
        mymap = defaultdict()
        mymap[0] = True
        def helper(end):
            if end in mymap:
                return mymap[end]
            res = False
            for i in wordDict:
                if s[0:end].endswith(i):
                    res = res or helper(end - len(i))
                    if res:
                        mymap[end] = res
                        return res
            mymap[end] = res
            return res
        res = helper(len(s))
        return res

sol = Solution()
res = sol.wordBreak(s = "applepenapple", wordDict = ["apple","pen"])
print(res)