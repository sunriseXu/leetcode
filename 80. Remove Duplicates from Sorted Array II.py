# Given an integer array nums sorted in non-decreasing order, remove some duplicates in-place such that each unique element appears at most twice. The relative order of the elements should be kept the same.

# Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums or len(nums) < 3:
            return len(nums)
        current = nums[0]
        repeat = 1
        idx = 1
        total = len(nums)
        while idx < total:
            if nums[idx] == current:
                if repeat < 2:
                    repeat += 1
                    idx += 1
                else:
                    nums.pop(idx)
                    total -= 1
            else:
                current = nums[idx]
                repeat = 1
                idx += 1
        return total

sol = Solution()
res = sol.removeDuplicates([1,1,1,2,2,3]) 
print(res)
