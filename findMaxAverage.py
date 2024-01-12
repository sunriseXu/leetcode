# You are given an integer array nums consisting of n elements, and an integer k.

# Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.
class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        res, l = float('-inf'), 0
        while l + k < len(nums) + 1:
            sum = 0
            for i in range(l, l + k):
                sum += nums[i]
            res = max(res, float(sum/k))
            l += 1
        return res
    def best(self, nums, k):
        res, l = float('-inf'), 0
        sum = 0 
        while l + k < len(nums) + 1:
            if l == 0:
                for i in range(l, l + k):
                    sum += float(nums[i])
            else:
                sum += float(nums[l + k - 1] - nums[l-1])
            res = max(res, sum/k)
            l += 1
        return res
sol = Solution()
res = sol.best([1,12,-5,-6,50,3], 4)
print(res)
