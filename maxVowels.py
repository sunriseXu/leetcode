# iven a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.

# Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.
class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        res, l = 0, 0
        sum = 0
        while l + k -1 < len(s):
            if l == 0:
                for i in range(0, k):
                    if s[i] in 'aeiou':
                        sum+=1
            else:
                if s[l-1] in 'aeiou':
                    sum -= 1
                if s[l+k-1] in 'aeiou':
                    sum += 1
            res = max(res, sum)
            l += 1
        return res


sol = Solution()
res = sol.maxVowels("abciiidef", 3)
print(res)