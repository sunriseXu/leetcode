# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        inorder =   [9,3,15,20,7], 
        postorder = [9,15,7,20,3]
        """
        self.inorderMap = {}
        idx = 0
        for i in inorder:
            self.inorderMap[str(i)] = idx
            idx += 1
        # root
        # left start, left end 
        # right start, right end
        
        root = self.construction(postorder, 0, len(postorder)-1, inorder, 0, len(inorder) - 1)
        return root
        
    def construction(self, postorder, pstart, pend, inorder, istart, iend):
        
        root = TreeNode()
        root.val = postorder[pend]
        if pstart == pend:
            return root
        mid = self.inorderMap[str(postorder[pend])]
        leftNum = mid - istart
        
        newPend = pstart + leftNum - 1

        if leftNum != 0:
            root.left = self.construction(postorder, pstart, newPend, inorder, istart, mid - 1)
        if iend - mid != 0:
            root.right = self.construction(postorder, newPend + 1, pend - 1, inorder, mid + 1, iend)
        return root

sol = Solution()
res = sol.buildTree(inorder = [9,3,15,20,7], postorder = [9,15,7,20,3])
print(res)