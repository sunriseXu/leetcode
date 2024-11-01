# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def flatten(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: None Do not return anything, modify root in-place instead.
        input a root
        return this root's result
        inside the function:
        left child return it's first and end 
        right child also return it's first and end
        then root.right = left.first
             left.last = right.first
        return root, right.end
        """
        
        def _flatten(root):
            
            if not root.left and not root.right:
                return root                
            if root.left:
                leftEnd = _flatten(root.left)
            if root.right:
                rightEnd = _flatten(root.right)
                
            if not root.left:
                return rightEnd
            if not root.right:
                root.right = root.left
                root.left = None
                return leftEnd

            tmp = root.right
            root.right = root.left
            leftEnd.right = tmp
            root.left = None
            return rightEnd
        if root:
            _flatten(root)
        


v3 = TreeNode(3)
v4 = TreeNode(4)
v2 = TreeNode(2, v3, None)
v6 = TreeNode(6)
v5 = TreeNode(5, None, v6)
v1 = TreeNode(1, v2, v5)
s = Solution()
res = s.flatten(v2)
print(res)