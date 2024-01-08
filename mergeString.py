class Solution:
    def mergeAlternately(self, str1, str2):
        strlen1 = len(str1)
        strlen2 = len(str2)
        longerLen = strlen1
        if longerLen < strlen2:
            longerLen = strlen2
        merged = ''
        for i in range(0, longerLen):
            if i < len(str1):
                merged += str1[i]
            if i < len(str2):
                merged += str2[i]
        return merged

sol = Solution()
res = sol.mergeAlternately("abcd","pq")
print(res)