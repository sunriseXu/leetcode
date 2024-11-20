class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        s = "babad"
        dp[start][end] = dp[start+1][end-1] + 2
        """
        dp = []
        maxLen = 1
        maxIdx = (0,0)
        for i in range(len(s)):
            tmp = [0] * len(s)
            dp.append(tmp)
        for i in range(len(s)):
            # init?
            currLen = len(s) - i
            for j in range(currLen):
                # print(j)
                # print(j+i)
                if i == 0:
                    dp[j][j+i] = 1
                elif i == 1:
                    if s[j] == s[j+i]:
                        dp[j][j+i] = 2
                        if maxLen < dp[j][j+i]:
                            maxLen = dp[j][j+i]
                            maxIdx = (j, j+i)
                else:
                    if dp[j+1][j+i-1] > 0 and s[j] == s[j+i]:
                        dp[j][j+i] += dp[j+1][j+i-1] + 2
                        if maxLen < dp[j][j+i]:
                            maxLen = dp[j][j+i]
                            maxIdx = (j, j+i)
        return s[maxIdx[0]:maxIdx[1]+1]

s = Solution()
res = s.longestPalindrome( "babad")
print(res)
                
        