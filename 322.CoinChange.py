class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        coins = [1,2,5], amount = 11
        5 + 5 + 1
        """
        if amount == 0:
            return 0
        from collections import defaultdict
        mymap = defaultdict()
        for i in coins:
            mymap[i] = 1
        minval = min(coins)
        def helper(total):
            if total in mymap:
                return mymap[total]
            if total < minval:
                return -1
            res = float("inf")
            for i in coins:
                tmp = helper(total - i)
                if tmp == -1:
                    continue
                res = min(res, tmp + 1)
            mymap[total] = res
            if res == float("inf"):
                return -1
            return res
        return helper(amount)

sol = Solution()
res = sol.coinChange([2], 3)
print(res)