class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        [10,9,2,5,3,7,101,18]
        
        """
        
        dp = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        maxLen = 0
        for i in dp:
            maxLen = max(maxLen, i)
        return maxLen

s = Solution()
res = s.lengthOfLIS([10,9,2,5,3,7,101,18])
print(res)