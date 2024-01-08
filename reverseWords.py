# Given an input string s, reverse the order of the words.

# A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

# Return a string of the words in reverse order concatenated by a single space.

# Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        tmp = s.split(' ')
        newS = [i for i in tmp if i]
        reversed = []
        newSLen = len(newS)
        for i in range(0, newSLen):
            reversed.append(newS[newSLen - i - 1])
        return ' '.join(reversed)
        
    def best(self, s):
        return

sol = Solution()
res = sol.reverseWords("leetcode dfd")
print(res)