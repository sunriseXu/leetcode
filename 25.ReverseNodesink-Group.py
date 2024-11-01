# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def reverseBetween(self, prev, head, right):
        """
        :type head: Optional[ListNode]
        :type left: int
        :type right: int
        :rtype: Optional[ListNode]
        """
        current = head
        leftPoint = head
        # reverse between
        next = leftPoint.next
        i = 1
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
        return head, leftPoint, end
    
    def reverseKGroup(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        prev = None
        newHead = head
        isStart = 1
        while True:
            # test length
            i = 1
            current = newHead
            flag = False
            while current.next:
                i += 1
                current = current.next
                if i == k:
                    flag = True
                    break
            if flag:
                origin , prev, newHead = self.reverseBetween(prev, newHead, k)
                if isStart:
                    head = origin
                if not newHead:
                    return head
            else:
                return head
            isStart = 0
        


s = Solution()

v5 = ListNode(5, None)
v4 = ListNode(4, v5)
v3 = ListNode(3, v4)
v2 = ListNode(2, v3)
v1 = ListNode(1, v2)

res = s.reverseKGroup(v1, 2)
print(res)