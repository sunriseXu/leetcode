# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        [4,2,1,3]
        5 7 8
        4 6 9 10
        """
        if not head or not head.next:
            return head
        # 注意fast一定要比slow多一步，不然当head.next为空时，slow和fast相同，无法区分左右了
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        mid = slow.next
        slow.next = None
        left = self.sortList(head)
        right = self.sortList(mid)
        
        dommy = ListNode(0)
        curr = dommy
        
        while left and right:
            if left.val < right.val:
                curr.next = left
                left = left.next
            else:
                curr.next = right
                right = right.next
            curr = curr.next
        curr.next = left or right
        return dommy.next
a = ListNode(3, None)
a = ListNode(1, a)
a = ListNode(2, a)
a = ListNode(4, a)

sol = Solution()
res = sol.sortList(a)
print(res.val) 
                
                
        
        