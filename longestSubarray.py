# Given a binary array nums, you should delete one element from it.

# Return the size of the longest non-empty subarray containing only 1's in the resulting array. Return 0 if there is no such subarray.
class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 11110111110110010111
        l, r = 0, 0
        res = 0
        lastZero = -1
        while r < len(nums):
            if nums[r] == 1:
                r += 1
            else:
                if lastZero >= l:
                    l = lastZero + 1
                lastZero = r
                r += 1
            res = max(res, r - l)
        return res - 1

sol = Solution()
res = sol.longestSubarray([0,1,1,1,0,1,1,0,1])
print(res)