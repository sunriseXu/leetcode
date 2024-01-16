# Given a binary tree root, a node X in the tree is named good if in the path from root to X there are no nodes with a value greater than X.

# Return the number of good nodes in the binary tree.

 

# Example 1:



# Input: root = [3,1,4,3,null,1,5]
# Output: 4
# Explanation: Nodes in blue are good.
# Root Node (3) is always a good node.
# Node 4 -> (3,4) is the maximum value in the path starting from the root.
# Node 5 -> (3,4,5) is the maximum value in the path
# Node 3 -> (3,1,3) is the maximum value in the path.

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        count = [0]
        def preOrder(root, res):
            # if root.left == None and root.right == None:
            res.sort()
            if not res or res[-1] <= root.val:
                count[0] += 1
                # return
            res.append(root.val)
            if root.left:
                newRes = list(res)
                preOrder(root.left, newRes)
            if root.right:
                newRes = list(res)
                preOrder(root.right, newRes)
        preOrder(root,[])
        return count[0]
    def best(self, root):
        if not root:
            return None
        count = [0]
        def dfs(root, maxVal):
            if root.val >= maxVal:
                count[0] += 1
                maxVal = root.val
            if root.left:
                dfs(root.left, maxVal)
            if root.right:
                dfs(root.right, maxVal)
        dfs(root, float('-inf'))
        return count[0]
tmp1 = TreeNode(3, None, None)
tmp3 = TreeNode(1, tmp1, None)
tmp1 = TreeNode(1, None, None)
tmp2 = TreeNode(5, None, None)
tmp1 = TreeNode(4, tmp1, tmp2)
tmp1 = TreeNode(3, tmp3, tmp1)
sol = Solution()
res = sol.best(tmp1)
print(res)