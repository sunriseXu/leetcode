# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        self.preorderMap = {}
        idx = 0
        for i in preorder:
            self.preorderMap[str(i)] = idx
            idx += 1
        
        self.inorderMap = {}
        idx = 0
        for i in inorder:
            self.inorderMap[str(i)] = idx
            idx += 1
        # root
        # left start, left end 
        # right start, right end
        
        root = self.construction(preorder, 0, len(preorder)-1, inorder, 0, len(inorder) - 1)
        return root
        
    def construction(self, preorder, pstart, pend, inorder, istart, iend):
        
        root = TreeNode()
        root.val = preorder[pstart]
        if pstart == pend:
            return root
        mid = self.inorderMap[str(preorder[pstart])]
        leftNum = mid - istart
        
        newPend = pstart + leftNum

        if leftNum != 0:
            root.left = self.construction(preorder, pstart + 1, newPend, inorder, istart, mid - 1)
        if iend - mid != 0:
            root.right = self.construction(preorder, newPend + 1, pend, inorder, mid + 1, iend)
        return root

sol = Solution()
res = sol.buildTree(preorder = [1,2], inorder = [2,1])
print(res)