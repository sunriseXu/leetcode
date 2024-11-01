# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: Optional[ListNode]
        :type left: int
        :type right: int
        :rtype: Optional[ListNode]
        """
        i = 1
        current = head
        prev = None
        while i < left:
            i += 1
            prev = current
            current = current.next
            # if i == left:
            #     break
        leftPoint = current
        # reverse between
        next = leftPoint.next
        i = left
        while i < right:
            tmp = next.next
            next.next = current
            
            current = next
            next = tmp
            i += 1
        rightPoint = current
        end = next
        if prev: 
            prev.next = rightPoint
        else:
            head = rightPoint
        leftPoint.next = end
        return head

s = Solution()

v5 = ListNode(5, None)
v4 = ListNode(4, v5)
v3 = ListNode(3, v4)
v2 = ListNode(2, v3)
v1 = ListNode(1, v2)

res = s.reverseBetween(v4, 1, 2)
print(res)