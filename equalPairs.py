# Given a 0-indexed n x n integer matrix grid, return the number of pairs (ri, cj) such that row ri and column cj are equal.

# A row and column pair is considered equal if they contain the same elements in the same order (i.e., an equal array).


class Solution(object):
    def equalPairs(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        import collections
        counter = collections.Counter()
        for i in grid:
            counter[tuple(i)] += 1
        res = 0
        for i in range(len(grid)):
            tmp = []
            for j in range(len(grid)):
                tmp.append(grid[j][i])
            res += counter[tuple(tmp)]
        return res

sol = Solution()
res = sol.equalPairs([[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]])
print(res)