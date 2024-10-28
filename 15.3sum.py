class Solution(object):
    def threeSum(self, nums):
        '''
        nums: List[int]
        rtype: List[List[int]]
        Input: nums = [-1,0,1,2,-1,-4]
        Output: [[-1,-1,2],[-1,0,1]]
        在一个数组中，找到三个数，相加等于0。穷尽所有组合。
        如果使用暴力遍历的方式，那么需要遍历数组三次。复杂度太高。
        1. 首先对数组进行排序
        2. 然后从两端开始进行筛选,但是如何对两端进行移动呢，无法解决这一问题
        3. 同时移动，还是只移动一端，如何判断移动哪一端？
        
        解答：
        1. 固定一端，然后对其他两端进行twosum
        
        该算法用途：
        用于配对问题上，例如那几个物体结合起来能达到特定效果，这和硬币DP问题有什么区别？
        硬币问题是硬币个数无限以及结合的数量并非固定
        '''
        res = []
        nums2 = sorted(nums)
        
        for i in range(len(nums2) - 2):
            if i > 0 and nums2[i] == nums2[i-1]:
                continue
            if nums2[i] > 0:
                continue
            j = i + 1
            k = len(nums2) - 1
            total = 0 - nums2[i]
            while j < k:
                tmp = nums2[j] + nums2[k] 
                if tmp < total:
                    j += 1
                elif tmp > total:
                    k -= 1
                else:
                    res.append([nums2[i], nums2[j], nums2[k]])
                    j += 1
                    while nums2[j] == nums2[j-1] and j < k:
                        j += 1
        return res
        
        
            
s = Solution()
res = s.threeSum([-1,0,1,2,-1,-4])
print(res)