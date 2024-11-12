class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        [1,2,1,3,5,6,4]
        left mid right
        left > mid kanou
        left < mid 
        right > mid  kanou
        right < mid  
        """
        if len(nums) == 1:
            return 0
        
        def findPeak(left, end):
            mid = (left + end) // 2
            if mid == 0 and nums[0] > nums[1]:
                return 0
            if mid == len(nums) - 1 and nums[-1] > nums[-2]:
                return len(nums) - 1
            if nums[mid-1] < nums[mid] and nums[mid] > nums[mid+1]:
                return mid
            if nums[left] > nums[mid]:
                return findPeak(left, mid - 1)
            if nums[end] > nums[mid]:
                return findPeak(mid + 1, end)
            if nums[mid+1] > nums[mid]:
                return findPeak(mid + 1, end)
            if nums[mid - 1] > nums[mid]:
                return findPeak(left, mid - 1)
            
        return findPeak(0, len(nums) - 1)

s = Solution()
res = s.findPeakElement([1,2,1,3,5,6,4])
print(res)