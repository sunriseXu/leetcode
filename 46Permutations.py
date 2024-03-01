class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        numsLen = len(nums)
        def helper(curr, res, exclude, numsLen):
            if len(curr) == numsLen:
                res.append(curr)
                return
            for i in range(0, numsLen):
                if i in exclude:
                    continue
                tmp = list(curr)
                tmp.append(nums[i])
                tmp2 = list(exclude)
                tmp2.append(i)
                helper(tmp, res, tmp2, numsLen)

        helper([], res, [], numsLen)
        return res
sol = Solution()
res = sol.permute([0, 1, 2])
print(res)