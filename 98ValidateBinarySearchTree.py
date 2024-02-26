# Given the root of a binary tree, determine if it is a valid binary search tree (BST).

# A valid BST is defined as follows:

# The left 
# subtree
#  of a node contains only nodes with keys less than the node's key.
# The right subtree of a node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees must also be binary search trees.

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        prev = [float('-inf')]
        result = [True]
        def isvalid(root):
            if root.left:
                isvalid(root.left)
            if root.val <= prev[0]:
                result[0] = False
                return 
            prev[0] = root.val
            if root.right:
                isvalid(root.right)
        if not root:
            return True
        isvalid(root)
        return result[0]
            
        