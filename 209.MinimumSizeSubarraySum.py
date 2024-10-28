class Solution(object):
    def minSubArrayLen(self, target, nums):
        '''
            固定数组，找一个长度最小的subarray,元素之和大于或等于某target
            [2,3,1,2,4,3] 7 -> [4,3] -> len 2
            注意是subarray而不是subset
            [1,4,4] 4 -> [4] -> len 1
            
            滑动窗口，不觉得像蜗牛吗，固定序列的顺序，找子序列的问题
            如果窗口合适，那记录下来，然后继续往前走
        '''
        i = 0
        j = 0
        minLen = float("inf")
        total = nums[0]
        while j < len(nums):
            if total >= target:
                minLen = min(minLen, j- i + 1)
                total -= nums[i]
                i += 1
                if i > j:
                    j += 1
                    if j > len(nums) - 1:
                        break
                    total += nums[j]
            else:
                j += 1
                if j > len(nums) - 1:
                    break
                total += nums[j]
        if minLen == float("inf"):
            minLen = 0
        return minLen
    
s = Solution()
res = s.minSubArrayLen(7, [2,3,1,2,4,3])
print(res)