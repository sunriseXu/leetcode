# You are given an integer array nums and an integer k.

# In one operation, you can pick two numbers from the array whose sum equals k and remove them from the array.

# Return the maximum number of operations you can perform on the array.
class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        pairedKeys = set()
        mydict = {}
        for i in range(0, len(nums)):
            val = nums[i]
            if val in mydict:
                mydict[val] = mydict[val]+1
            else:
                mydict[val] = 1
        paired = 0
        for key in mydict.keys():
            if key in pairedKeys:
                continue
            matched = k - key
            if matched not in mydict:
                continue
            pairedKeys.add(key)
            pairedKeys.add(matched)
            val = mydict[key]
            matchedVal = mydict[matched]
            if key == matched:
                paired += int(val / 2)
            else:
                paired += min(val, matchedVal)
        return paired
    def best1(self, nums, k):
        import collections
        res, mydict = 0, collections.Counter(nums)
        for key, val in mydict.items():
            matched = k - key
            if matched not in mydict or matched < key:
                continue
            res += min(val, mydict[matched]) if key != matched else val//2
        return res
    def best2(self, nums, k):
        nums.sort()
        
        
        
sol = Solution()
res = sol.best1([3,1,3,4,3], 6)
print(res)