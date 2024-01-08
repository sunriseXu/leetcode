class Solution(object):
    def gcdOfStrings(self, str1, str2):
        strLen1 = len(str1)
        strLen2 = len(str2)
        smaller = str1
        longer = str2
        if strLen1 > strLen2:
            smaller = str2
            longer = str1
        divider = 1
        smallerLen = len(smaller)
        longerLen = len(longer)
        current = ''
        while divider <= smallerLen:
            if smallerLen % divider != 0 or longerLen % divider !=0:
                divider += 1
                continue
            smallerDiv = int(smallerLen / divider)
            longerDiv = int(longerLen / divider)
            smallerMerge = smaller[0:divider] * smallerDiv
            longerMerge = smaller[0:divider] * longerDiv
            if smallerMerge == smaller and longerMerge == longer:
                current = smaller[0:divider]
            divider += 1
        return current

sol = Solution()
res = sol.gcdOfStrings("ab", "abab")
print(res)