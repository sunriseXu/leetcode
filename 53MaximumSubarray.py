class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        [-2,1,-3,4,-1,2,1,-5,4]
        [4,-1,2,1]
        """
        arr = [0]
        maxSum = float('-inf')
        for i in range(len(nums)):
            arr.append(max(arr[-1] + nums[i], nums[i]))
            maxSum = max(arr[-1], maxSum)
        return maxSum

sol = Solution()
res = sol.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
print(res)