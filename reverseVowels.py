# Given a string s, reverse only all the vowels in the string and return it.

# The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

class Solution(object):
    # my solution
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U']
        allVowels = []
        allIdx = []
        tmps = []
        for i in range(0, len(s)):
            tmps.append(s[i])
            if s[i] in vowels:
                allVowels.append(s[i])
                allIdx.append(i)
        allVLen = len(allVowels)
        for i in range(0, allVLen):
            tmps[allIdx[i]] = allVowels[allVLen - i - 1]
        return ''.join(tmps)
    # best solution
    def best(self, s):
        word = list(s)
        start = 0
        end = len(word) - 1
        vowels = "aeiouAEIOU"
        
        while start < end:
            if word[start] not in vowels:
                start += 1
                continue
            if word[end] not in vowels:
                end -= 1
                continue
            tmp = word[start]
            word[start] = word[end]
            word[end] = tmp
            start += 1
            end -= 1
        return ''.join(word)
        


sol = Solution()
res = sol.best("leetcode")
print(res)