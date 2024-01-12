# Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        l, r = 0, 0
        res = 0
        zeros = 0
        while r < len(nums):
            if zeros < k:
                zeros += 1 - nums[r]
                r += 1
            elif nums[r] == 1:
                r += 1
            else:
                zeros -= 1 - nums[l]
                l += 1
            res = max(res, r - l)    
        return res

sol = Solution()
res = sol.longestOnes([1,1,1,0,0,0,1,1,1,1,0], k = 2)

print(res)