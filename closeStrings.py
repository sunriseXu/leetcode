# Two strings are considered close if you can attain one from the other using the following operations:

# Operation 1: Swap any two existing characters.
# For example, abcde -> aecdb
# Operation 2: Transform every occurrence of one existing character into another existing character, and do the same with the other character.
# For example, aacabb -> bbcbaa (all a's turn into b's, and all b's turn into a's)
# You can use the operations on either string as many times as necessary.

# Given two strings, word1 and word2, return true if word1 and word2 are close, and false otherwise.
# Example 1:

# Input: word1 = "abc", word2 = "bca"
# Output: true
# Explanation: You can attain word2 from word1 in 2 operations.
# Apply Operation 1: "abc" -> "acb"
# Apply Operation 1: "acb" -> "bca"
# Example 2:

# Input: word1 = "a", word2 = "aa"
# Output: false
# Explanation: It is impossible to attain word2 from word1, or vice versa, in any number of operations.
# Example 3:

# Input: word1 = "cabbba", word2 = "abbccc"
# a 2 b 3 c 1
# a 1 b 2 c 3
# Output: true
# Explanation: You can attain word2 from word1 in 3 operations.
# Apply Operation 1: "cabbba" -> "caabbb"
# Apply Operation 2: "caabbb" -> "baaccc"
# Apply Operation 2: "baaccc" -> "abbccc"

class Solution(object):
    def closeStrings(self, str1, str2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """
        import collections
        counterStr1 = collections.Counter(str1)
        counterStr2 = collections.Counter(str2)

        keys1 = set(counterStr1.keys())
        keys2 = set(counterStr2.keys())



        count1 = list(counterStr1.values())
        count2 = list(counterStr2.values())
        count1.sort()
        count2.sort()

        if keys1 == keys2 and count1 == count2:
            return True
        return False




sol = Solution()
res = sol.closeStrings("a", "aa")
print(res)