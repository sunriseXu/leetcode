class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        # sort the cite
        citations.sort()
        m = len(citations)
        hindex = 0
        for i in range(m-1, -1, -1):
            if citations[i] >= m - i:
                hindex = m -i 
        return hindex
    
s = Solution()
res = s.hIndex([3,0,6,1,5])
print(res)


# [4]
# 0 1 2 6 7 8


