# Consider all the leaves of a binary tree, from left to right order, the values of those leaves form a leaf value sequence.



# For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9, 8).

# Two binary trees are considered leaf-similar if their leaf value sequence is the same.

# Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.

 

# Example 1:


# Input: root1 = [3,5,1,6,2,9,8,null,null,7,4], root2 = [3,5,1,6,7,4,2,null,null,null,null,null,null,9,8]
# Output: true

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        def postOrder(root, res):
            if root == None:
                return 
            if root.left == None and root.right == None:
                res.append(root.val)
            postOrder(root.left, res)
            postOrder(root.right, res)
            
        res = []
        postOrder(root1, res)
        res2 = []
        postOrder(root2, res2)
        return True if res==res2 else False

tmp1 = TreeNode(15, None, None)
tmp2 = TreeNode(7, None, None)
tmp1 = TreeNode(20, tmp1, tmp2)
tmp2 = TreeNode(9, None, None)
tmp1 = TreeNode(3, tmp2, tmp1)
sol = Solution()
res = sol.leafSimilar(tmp1, tmp1)
print(res)