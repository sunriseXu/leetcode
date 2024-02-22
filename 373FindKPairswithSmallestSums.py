class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        import heapq
        res = []
        class MyPair(object):
            def __init__(self, ele):
                self.a = ele
                self.sum = ele[0] + ele[1]
            def getsum(self):
                return self.sum
            def getele(self):
                return self.a
            def __lt__(self, nxt):
                return self.sum < nxt.sum
        for i in nums1:
            for j in nums2:
                heapq.heappush(res, MyPair([i, j]))
        nsmall = heapq.nsmallest(k, res)
        finalres = []
        for i in nsmall:
            finalres.append(i.getele())
        return finalres
    def kSmallestPairs2(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        import heapq
        res = []
        class MyPair(object):
            def __init__(self, ele):
                self.a = ele
                self.sum = ele[0] + ele[1]
            def getsum(self):
                return self.sum
            def getele(self):
                return self.a
            def __lt__(self, nxt):
                return self.sum > nxt.sum
        flag = False
        for i in nums1:
            idx2 = 0
            for j in nums2:
                idx2 += 1
                curr = MyPair([i, j])
                heapq.heappush(res, curr)
                if len(res) > k:
                    top = heapq.heappop(res)
                    if curr == top or curr.getsum()==top.getsum():
                        if idx2 == 1:
                            flag = True
                        break
            if flag:
                break
        finalres = []
        for i in res:
            finalres.append(i.getele())
        return finalres
    
sol = Solution()
res = sol.kSmallestPairs2(nums1 = [1,1,2], nums2 = [1,2,3], k = 2)
print(res)      