# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        count = [0]
        kmallest = [0]
        def traverse(root):
            if root.left:
                traverse(root.left)
            count[0] += 1
            if count[0] == k:
                kmallest[0] = root.val
                return root.val
            if root.right:
                traverse(root.right)
        
        traverse(root)
        return kmallest[0]
    def kthSmallest2(self, root, k):
        stack = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            k -= 1
            if k == 0:
                return root.val
            root = root.right
                 
            