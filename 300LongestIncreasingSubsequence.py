class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        [10,9,2,5,3,7,101,18]
        10
        9
        2
        2 5
        2 3
        2 5 7 / 2 3 7
        2 5 7 101 / 2 3 7 101
        2 5 7 18 / 2 3 7 18
        """
        dp = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        res = 0
        for i in range(len(nums)):
            res = max(res, dp[i])
        return res

sol = Solution()
res = sol.lengthOfLIS([10,9,2,5,3,7,101,18])
print(res)