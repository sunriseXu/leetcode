# Given an array of characters chars, compress it using the following algorithm:

# Begin with an empty string s. For each group of consecutive repeating characters in chars:

# If the group's length is 1, append the character to s.
# Otherwise, append the character followed by the group's length.
# The compressed string s should not be returned separately, but instead, be stored in the input character array chars. Note that group lengths that are 10 or longer will be split into multiple characters in chars.

# After you are done modifying the input array, return the new length of the array.

# You must write an algorithm that uses only constant extra space.

class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        res = []
        current = ''
        count = 0
        for ch in chars:
            if ch == current:
                count += 1
            else:
                if count > 1:
                    tmp = list(str(count))
                    res.extend(tmp)
                res.append(ch)
                current = ch
                count = 1
        if count > 1:
            tmp = list(str(count))
            res.extend(tmp)
        for i in range(0, len(res)):
            chars[i] = res[i]
        return len(res)
    def best(self, chars):
        # two pointers solution, space o(1)
        current = 0
        flag = 0
        count = 0
        while flag < len(chars):
            if chars[current] == chars[flag]:
                count += 1
            else:
                if count > 1:
                    tmp = list(str(count))
                    for i in range(0, len(tmp)):
                        current += 1
                        chars[current] = tmp[i]
                current += 1
                chars[current] = chars[flag] 
                count = 1
            flag += 1
        if count > 1:
            tmp = list(str(count))
            for i in range(0, len(tmp)):
                current += 1
                chars[current] = tmp[i]
        return current + 1
sol = Solution()
res = sol.best(["a","b","b","b","b","b","b","b","b","b","b","b","b"])
print(res)