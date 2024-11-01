# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        maxValue = [-float("inf")]
        
        def maxPath(root):
            if not root.left and not root.right:
                maxValue[0] = max(maxValue[0], root.val)
                return root.val
            leftVal, rightVal = 0, 0
            if root.left:
                leftVal = maxPath(root.left)
                maxValue[0] = max(maxValue[0], leftVal)
            if root.right:
                rightVal = maxPath(root.right)
                maxValue[0] = max(maxValue[0], rightVal)
            # if want to link
            # root -> can link 
            # left + root -> can link
            # right + root -> can link
            # left -> can not link any more, in to set
            # right -> can not link any more, in to set
            # root + left + right -> can not link any more, in to set
            
            # to not link case
            maxValue[0] = max(maxValue[0], leftVal+rightVal+root.val)
            
            # to link case
            linkMax = max(leftVal + root.val, root.val)
            linkMax = max(rightVal + root.val, linkMax)
            return linkMax
        rootVal = maxPath(root)
        return max(maxValue[0], rootVal)
v9 = TreeNode(9)
v15 = TreeNode(15)
v7 = TreeNode(7)
v20 = TreeNode(20, v15, v7)
root = TreeNode(-10, v9, v20)
s = Solution()
res = s.maxPathSum(root)