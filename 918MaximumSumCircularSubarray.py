class Solution(object):
    def maxSubarraySumCircular(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 1. max sum array is not circular, we just record max sum
        # 1. max sum array is circular, then min sum is not circular, we record min sum
        maxCurr = nums[0]
        maxSum = nums[0]
        minCurr = nums[0]
        minSum = nums[0]
        total = nums[0]
        for num in nums[1:]:
            total += num
            maxCurr = max(maxCurr+num, num)
            maxSum = max(maxCurr, maxSum)
            
            minCurr = min(minCurr + num, num)
            minSum = min(minSum, minCurr)
        if total == minSum:
            return maxSum
        return max(maxSum, total - minSum)

s = Solution()
res = s.maxSubarraySumCircular([-3,-2,-3])
print(res)