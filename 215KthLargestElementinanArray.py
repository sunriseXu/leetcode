class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        import heapq
        heapq.heapify(nums)
        res = heapq.nlargest(k, nums)
        return res[-1]
    def findKthLargest2(self, nums, k):
        import heapq
        res = []
        for i in nums:
            heapq.heappush(res, i)
            if len(res) > k:
                heapq.heappop(res)
        return res[0]
        
sol = Solution()
res = sol.findKthLargest2([3,2,3,1,2,4,5,5,6], 4)
print(res)