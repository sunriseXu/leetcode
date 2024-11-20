class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        coins = [1,2,5], amount = 11
        5 + 5 + 1
        """
        minDict = {}
        def dp(amount):
            if amount == 0:
                return 0
            if amount < 0:
                return -1
            if amount in minDict:
                if minDict[amount] != -1:
                    return minDict[amount]
                else:
                    return -1
            minSum = float("inf")
            for coin in coins:
                res = dp(amount - coin)
                if res >= 0:
                    minSum = min(minSum, res)
            if minSum != float("inf"):
                minDict[amount] = minSum + 1
            else:
                minDict[amount] = -1
            return minDict[amount]
        return dp(amount)

s = Solution()
res = s.coinChange([2], 0)
print(res)