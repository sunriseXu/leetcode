# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        allNums = []
        def reSum(root, total):
            if not root.left and not root.right:
                allNums.append(total*10 + root.val)
                return root.val
            if root.left:
                reSum(root.left, total*10 + root.val)
            if root.right:
                reSum(root.right, total*10 + root.val)

        reSum(root, 0)
        total = 0
        for i in allNums:
            total += i
        return total

v5 = TreeNode(5)
v1 = TreeNode(1)
v0 = TreeNode(0)
v9 = TreeNode(9, v5, v1)
v4 = TreeNode(4, v9, v0)
res = Solution()
ress = res.sumNumbers(v4)

        
        