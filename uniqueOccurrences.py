# Given an array of integers arr, return true if the number of occurrences of each value in the array is unique or false otherwise.
# Input: arr = [1,2,2,1,1,3]
# Output: true
# Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.
class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        import collections
        coun = collections.Counter(arr)
        values = coun.values()
        occurence = []
        for i in values:
            if i not in occurence:
                occurence.append(i)
            else:
                return False
        return True
sol = Solution()
res = sol.uniqueOccurrences([1,2 ,2,2,1,1,3])
print(res)