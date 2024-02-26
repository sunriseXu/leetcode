# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # inorder traverse
        # binary search tree
        inorder = []
        def traverse(root):
            if root.left:
                traverse(root.left)
            if root:
                inorder.append(root.val)
            if root.right:
                traverse(root.right)
        traverse(root)
        res = float('inf')
        for i in range(len(inorder) - 1):
            curr = inorder[i]
            next = inorder[i + 1]
            tmp = abs(curr - next)
            res = min(tmp, res)
        return res

sol = Solution()
res = sol.getMinimumDifference()
print(res)
