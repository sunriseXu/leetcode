# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        queue = []
        queue2 = []
        output = []
        if not root:
            return []
        queue.append(root)
        output.append([root.val])
        tmp  = []
        while queue:
            current = queue.pop(0)
            if current.left:
                tmp.append(current.left.val)
                queue2.append(current.left)
            if current.right:
                tmp.append(current.right.val)
                queue2.append(current.right)
            
            if not queue:
                if tmp:
                    output.append(tmp)
                tmp = []
                queue = queue2
                queue2 = []
        return output
n15 = TreeNode(15)
n7 = TreeNode(7)
n20 = TreeNode(20, n15, n7)
n9 = TreeNode(9)
n3 = TreeNode(3, n9, n20)
 
s = Solution()
res = s.levelOrder(n3)
print(res)
            
        