# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        build search tree from sorted array, high balanced
        divide array to 2 same length part
        """
        def buildTree(array):
            if not array:
                return None
            root = TreeNode()
            mid = len(array) // 2
            root.val = array[mid]
            root.left = buildTree(array[0 : mid])
            root.right = buildTree(array[mid + 1 :])
            return root
        return buildTree(nums)
        
sol = Solution()
res = sol.sortedArrayToBST([-10,-3,0,5,9])
print(res)