# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

# Note that you must do this in-place without making a copy of the array.

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        i = 0
        j = len(nums)
        k = 0
        while k < j:
            if nums[i] == 0:
                nums.append(nums[i])
                nums.pop(i)
            else:
                i += 1
            k += 1
    def best(self, nums):
        current = 0
        flag = 0
        while flag < len(nums):
            if nums[flag] != 0:
                nums[current] = nums[flag]
                current += 1
            flag += 1
        while current < len(nums):
            nums[current] = 0
            current += 1
        return nums
                
                
sol = Solution()
res = sol.best([0,1,0,3,12])
print(res)