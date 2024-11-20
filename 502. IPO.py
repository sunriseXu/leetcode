class Solution(object):
    def findMaximizedCapital(self, k, w, profits, capital):
        """
        :type k: int
        :type w: int
        :type profits: List[int]
        :type capital: List[int]
        :rtype: int
        """
        import heapq
        maxProfit = []
        minCapital = [(c, p) for c, p in zip(capital, profits)]
        heapq.heapify(minCapital)
        # c is no decendency oder
        for i in range(k):
        
            while minCapital and minCapital[0][0] <= w:
                # we get all project we can afford currently
                c, p = heapq.heappop(minCapital)
                # push them in to heap with order
                heapq.heappush(maxProfit, -1 * p)
            if not maxProfit:
                break
            # now, pick up largest profit and add to capital
            w += -1 * heapq.heappop(maxProfit)
        return w

s = Solution()
res = s.findMaximizedCapital(k = 2, w = 0, profits = [1,2,3], capital = [0,1,1])
print(res)