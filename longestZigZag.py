# You are given the root of a binary tree.

# A ZigZag path for a binary tree is defined as follow:

# Choose any node in the binary tree and a direction (right or left).
# If the current direction is right, move to the right child of the current node; otherwise, move to the left child.
# Change the direction from right to left or from left to right.
# Repeat the second and third steps until you can't move in the tree.
# Zigzag length is defined as the number of nodes visited - 1. (A single node has a length of 0).

# Return the longest ZigZag path contained in that tree.

 

# Example 1:


# Input: root = [1,null,1,1,1,null,null,1,1,null,1,null,null,null,1]
# Output: 3
# Explanation: Longest ZigZag path in blue nodes (right -> left -> right).

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def longestZigZag(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        count = [0]
        def dfs(root, last, length):
            if last == 'r' or last == '':
                if root.left:
                    dfs(root.left, 'l', length+1)               
                if root.right:
                    count[0] = max(count[0], length)
                    dfs(root.right, 'r', 1)

            if last == 'l' or last == '':
                if root.right:
                    dfs(root.right, 'r', length+1)
                if root.left:
                    count[0] = max(count[0], length)
                    dfs(root.left, 'l', 1)
            if not root.left and not root.right:
                count[0] = max(count[0], length)
                
        dfs(root, '', 0)
        return count[0]
# [1,1,1,1,null,1,1,null,null,1,null,1,null,null,1,null,1]



tmp3 = TreeNode(3, None, None)
tmp2 = TreeNode(2, tmp3, None)

tmp9 = TreeNode(9, None, None)
tmp10 = TreeNode(10, None, None)

tmp7 = TreeNode(7, None, tmp9)
tmp5 = TreeNode(5, tmp7, None)

tmp8 = TreeNode(8, None, tmp10)
tmp6 = TreeNode(6, tmp8, None)

tmp4 = TreeNode(4, tmp5, tmp6)


tmp1 = TreeNode(1, tmp2, tmp4)

sol = Solution()
res = sol.longestZigZag(tmp1)
print(res)