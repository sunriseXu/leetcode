# Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

 

# Example 1:

# Input: nums = [1,2,3,4,5,6,7], k = 3
# Output: [5,6,7,1,2,3,4]
# Explanation:
# rotate 1 steps to the right: [7,1,2,3,4,5,6]
# rotate 2 steps to the right: [6,7,1,2,3,4,5]
# rotate 3 steps to the right: [5,6,7,1,2,3,4]

class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        total = len(nums)
        k = k % total
        if k == 0:
            return nums
        nums[0: k], nums[k:-1] = nums[k:-1], nums[0: k]
        return nums
    
sol = Solution()
res = sol.rotate(nums = [1,2,3,4,5,6,7], k = 3)
print(res)