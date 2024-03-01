class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        n = 4, k = 2
        1, 2, 3, 4
        [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
        """
        # combination
        def bfs(path, res, num, start):
            if num == 0:
                res.append(path)
                return
            for i in range(start, n + 1):
                tmp = list(path)
                tmp.append(i)
                bfs(tmp, res, num - 1, i + 1)
        res = []
        bfs([], res, k, 1)
        return res

sol = Solution()
res = sol.combine(n = 4, k = 2)
print(res)