# Given an integer array nums, return true if there exists a triple of indices (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k]. If no such indices exists, return false.

class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # [2,1,5,0,4,6] 2 5 3 1 4
        first = second = float("inf")
        for i in nums:
            if i <= first:
                first = i
            elif i <= second:
                second = i
            else:
                return True
        return False

sol = Solution()
res = sol.increasingTriplet([2,1,5,0,4,6])
print(res)