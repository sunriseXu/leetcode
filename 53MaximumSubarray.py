class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        [-2,1,-3,4,-1,2,1,-5,4]
        [4,-1,2,1]
        """
        maxsum = nums[0]
        currSum = 0
        for num in nums:
            currSum = max(currSum+num, num)
            maxsum = max(currSum, maxsum)
        return maxsum

sol = Solution()
res = sol.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
print(res)