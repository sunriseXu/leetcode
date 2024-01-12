# Given an array of integers nums, calculate the pivot index of this array.

# The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.

# If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left. This also applies to the right edge of the array.

# Return the leftmost pivot index. If no such index exists, return -1.
class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        tmp = [0] * len(nums)
        for i in range(1, len(nums)):
            tmp[i] = tmp[i-1] + nums[i - 1]
        lastEqual = -1
        rightsum = 0
        for i in range(len(nums) - 1, -1, -1):
            if tmp[i] == rightsum:
                lastEqual = i
            rightsum += nums[i]
        return lastEqual
sol = Solution()
res = sol.pivotIndex([1,7,3,6,5,6])
print(res)