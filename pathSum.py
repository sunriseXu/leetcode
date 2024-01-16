# Given the root of a binary tree and an integer targetSum, return the number of paths where the sum of the values along the path equals targetSum.

# The path does not need to start or end at the root or a leaf, but it must go downwards (i.e., traveling only from parent nodes to child nodes).

 

# Example 1:


# Input: root = [10,5,-3,3,2,null,11,3,-2,null,1], targetSum = 8
# Output: 3
# Explanation: The paths that sum to 8 are shown.

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: int
        """
        if not root:
            return 0
        count = [0]
        def dfs(root, res):
            for i in range(len(res)):
                res[i] += root.val
                if res[i] == targetSum:
                    count[0] += 1
            if  root.val == targetSum:
                count[0] += 1
            res.append(root.val)
            if root.left:
                newRes = list(res)
                dfs(root.left, newRes)
            if root.right:
                newRes = list(res)
                dfs(root.right, newRes)
        dfs(root, [])
        return count[0]
    
tmp1 = TreeNode(15, None, None)
tmp2 = TreeNode(7, None, None)
tmp1 = TreeNode(20, tmp1, tmp2)
tmp2 = TreeNode(9, None, None)
tmp1 = TreeNode(3, tmp1, tmp2)
sol = Solution()
res = sol.pathSum(tmp1, 12)
print(res)

                
