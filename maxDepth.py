# Given the root of a binary tree, return its maximum depth.

# A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

 

# Example 1:


# Input: root = [3,9,20,null,null,15,7]
# Output: 3
# Definition for a binary tree node.

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        left = self.maxDepth(root.left) + 1
        right = self.maxDepth(root.right) + 1
        return max(left, right)
    def bfs(self, root):
        queue = [root] if root else []
        res = 0
        while queue:
            res += 1 
            currentQ = []
            for current in queue:
                if current.left:
                    currentQ.append(current.left)
                if current.right:
                    currentQ.append(current.right)
            queue = currentQ
        return res

tmp1 = TreeNode(15, None, None)
tmp2 = TreeNode(7, None, None)
tmp1 = TreeNode(20, tmp1, tmp2)
tmp2 = TreeNode(9, None, None)
tmp1 = TreeNode(3, tmp1, tmp2)
sol = Solution()
res = sol.bfs(tmp1)
print(res)