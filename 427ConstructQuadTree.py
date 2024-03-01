
# Definition for a QuadTree node.
class Node(object):
    def __init__(self, val=False, isLeaf=False, topLeft=None, topRight=None, bottomLeft=None, bottomRight=None):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


class Solution(object):
    def construct(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: Node
        """
        
        def helper(x, y, size):
            if size == 1:
                if grid[x][y] == 1:
                    res = True
                else:
                    res = False
                return res, True, None
            
            a = size // 2
            topLeftVal, topLeftLeaf, topLeftNode = helper(x, y, a)
            topRightVal, topRightLeaf, topRightNode = helper(x, y + a, a)
            bottomLeftVal, bottomLeftLeaf, bottomLeftNode = helper(x + a, y, a)
            bottomRightVal, bottomRightLeaf, bottomRightNode = helper(x + a, y + a, a)
            
            if topLeftVal == topRightVal and topRightVal == bottomLeftVal and bottomLeftVal == bottomRightVal \
                and topLeftLeaf and topRightLeaf and bottomLeftLeaf and bottomRightLeaf:
                return topLeftVal, True, None
            else:
                # 4 grid not the same, so we should create 4 nodes and return root nodes
                root = Node(False, False)
                root.topLeft = topLeftNode or Node(topLeftVal, topLeftLeaf)
                root.topRight = topRightNode or Node(topRightVal, topRightLeaf)
                root.bottomLeft = bottomLeftNode or Node(bottomLeftVal, bottomLeftLeaf)
                root.bottomRight = bottomRightNode or Node(bottomRightVal, bottomRightLeaf)
                return False, False, root
        _, _, root = helper(0, 0, len(grid))
        if not root:
            return Node(grid[0][0], True)
        return root

sol = Solution()
res = sol.construct([[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0]])
print(res)