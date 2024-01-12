# Given two 0-indexed integer arrays nums1 and nums2, return a list answer of size 2 where:

# answer[0] is a list of all distinct integers in nums1 which are not present in nums2.
# answer[1] is a list of all distinct integers in nums2 which are not present in nums1.
# Note that the integers in the lists may be returned in any order.
class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """
        tmp1, tmp2 = set(), set()
        len1 = len(nums1)
        len2 = len(nums2)
        length = max(len1, len2)
        for i in range(length):
            if i < len1 and nums1[i] not in nums2:
                tmp1.add(nums1[i])
            if i < len2 and nums2[i] not in nums1:
                tmp2.add(nums2[i])
        return [list(tmp1), list(tmp2)]


        
sol = Solution()
res = sol.findDifference([1, 3, 5], [1, 2, 4])
print(res)