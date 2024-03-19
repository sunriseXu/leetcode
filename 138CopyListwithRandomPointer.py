
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        [[3,null],[2,0],[1,null]]
        """
        
        cacheMap = {}
        
        curr = head 
        newCurr = None
        last = None
        newHead = None
        while curr:
            val = curr.val
            newCurr = Node(val)
            if last:
                last.next = newCurr
            else:
                newHead = newCurr
            cacheMap[curr] = newCurr
            last = newCurr
            curr = curr.next
        
        curr = head
        newCurr = newHead
        while curr:
            random = curr.random
            mirrorRandom = None
            if random:
                mirrorRandom = cacheMap[random]
            newCurr.random = mirrorRandom
            
            curr = curr.next
            newCurr = newCurr.next
        return newHead


a = Node(3)
b = Node(2)
c = Node(1)

a.next = b
b.next = c 
b.random = a 

sol = Solution()
res = sol.copyRandomList(a)
print(res)
        