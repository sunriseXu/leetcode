class Solution(object):
    def rob(self, nums):
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        last = 0
        current = nums[0]
        for i in range(1, len(nums)):
            tmp = current
            current = max(current, last + nums[i])
            last = tmp
        return current
s = Solution()
res = s.rob([1,2,3,1])
print(res)