class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        def binarySearch(start, end):
            if start > end:
                return -1
            if start == end:
                if nums[start] == target:
                    return start
                else:
                    return -1 
            mid = (start + end) // 2
            if target < nums[mid]:
                return binarySearch(start, mid - 1)
            elif nums[mid] < target:
                return binarySearch(mid + 1, end)
            else:
                return mid
        
        
        def rotateSearch(start, end):
            if start == end:
                if nums[start] == target:
                    return start
                else:
                    return -1
            mid = (start + end) // 2
            if nums[start] <= target <= nums[mid]:
                return binarySearch(start, mid)
            if nums[mid] <= target <= nums[end]:
                return binarySearch(mid, end)
            if nums[start] <= nums[mid]:
                return rotateSearch(mid+1, end)
            else:
                return rotateSearch(start, mid)
        return rotateSearch(0, len(nums) - 1)
s = Solution()
res = s.search(nums =[4,5,6,7,0,1,2], target = 0)
print(res)