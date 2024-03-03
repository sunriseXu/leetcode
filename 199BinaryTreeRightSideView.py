# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        queue = []
        if root == None:
            return []
        queue.append(root)
        res = []
        while queue:
            tmpQueue = []
            res.append(queue[-1].val)
            for i in queue:
                if i.left:
                    tmpQueue.append(i.left)
                if i.right:
                    tmpQueue.append(i.right)
            queue = tmpQueue
        return res

a = TreeNode(5)
b = TreeNode(2, left=None, right=a)
c = TreeNode(4)
d = TreeNode(3, None, c)
e = TreeNode(1, b, d)
sol = Solution()
res = sol.rightSideView(e)
print(res)