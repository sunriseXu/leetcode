
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return root
        queue = []
        queue.append(root)
        while queue:
            tmpQueue = []
            last = None
            for i in queue:
                if last:
                    last.next = i
                last = i
                if i.left:
                    tmpQueue.append(i.left)
                if i.right:
                    tmpQueue.append(i.right)
            queue = tmpQueue
        return root
            
