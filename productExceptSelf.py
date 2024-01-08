# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

# You must write an algorithm that runs in O(n) time and without using the division operation.

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        numsLen = len(nums)
        leftProduction = [1] * numsLen
        for i in range(0, numsLen):
            if i > 0:
                leftProduction[i] = leftProduction[i-1] * nums[i - 1]
        rightProduction = [1] * numsLen
        for i in range(numsLen-1, -1, -1):
            if i < numsLen - 1:
                rightProduction[i] = rightProduction[i+1] * nums[i + 1]
        res = []
        for i in range(0, numsLen):
            res.append(leftProduction[i]*rightProduction[i])
        return res
    def best(self, nums):
        length = len(nums)
        products = [1] * length
        for i in range(1, length):
            products[i] = products[i-1] * nums[i-1]
        right = nums[-1]
        for i in range(length - 2, -1, -1):
            products[i] *= right
            right *= nums[i]
        return products

sol = Solution()
res = sol.best([-1,1,0,-3,3])
print(res)
            