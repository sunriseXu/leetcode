# Given the head of a singly linked list, reverse the list, and return the reversed list.

 
# 1 2 3 4 5
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        current, last = head, None
        while current != None:
            # current to last
            nextNode = current.next 
            current.next = last
            
            # move last and current
            last = current
            current = nextNode
        return last
    


tmp = ListNode(5, None)
tmp = ListNode(4, tmp)
tmp = ListNode(3, tmp)
tmp = ListNode(2, tmp)
tmp = ListNode(1, tmp)

sol = Solution()
res = sol.reverseList(tmp)