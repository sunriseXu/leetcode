class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        [2,7,9,3,1]
        12
        2 -> 2
        2 7 -> 7
        2 7 9 -> 11
        2 7 9 3 -> 11
        """
        if len(nums) == 1:
            return nums[0]
        from collections import defaultdict
        self.map = defaultdict()
        self.map[0] = nums[0]
        self.map[1] = max(nums[0], nums[1])
        def helper(n):
            # must rob last
            # don't rob last
            if n in self.map:
                return self.map[n]
            res = max(helper(n-1), helper(n-2) + nums[n])
            self.map[n] = res
            return res
        return helper(len(nums) - 1)
sol = Solution()
res = sol.rob([2, 7, 9, 3, 1])
print(res)