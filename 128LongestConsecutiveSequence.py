class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        visited = set()
        maxLen = 0
        for i in nums:
            if i in visited:
                continue
            currLen = 1
            up = i + 1
            
            if up in nums:
                while True:
                    if up in nums:
                        currLen += 1
                        visited.add(up)
                    else:
                        break
                    up += 1
                    
            down = i - 1
            if down in nums:
                while True:
                    if down in nums:
                        currLen += 1
                        visited.add(down)
                    else:
                        break
                    down -= 1
            maxLen = max(maxLen, currLen) 
        return maxLen
    def longestConsecutive2(self, nums):
        maxLen = 0
        nums = set(nums)
        for i in nums:
            if i - 1 in nums:
                continue
            currLen = 1
            while i + 1 in nums:
                currLen += 1
                i += 1
            maxLen = max(maxLen, currLen)
        return maxLen
        
sol = Solution()
res = sol.longestConsecutive2([0,3,7,2,5,8,4,6,0,1])
print(res)
        