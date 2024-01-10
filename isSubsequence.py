# Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

# A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).
class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        first = 0 
        second = 0
        while first < len(s) and second < len(t):
            if s[first] == t[second]:
                first += 1
                second += 1
            else:
                second += 1
        return first == len(s)
    
sol = Solution()
res = sol.isSubsequence("axc", "ahbgdc")
print(res)