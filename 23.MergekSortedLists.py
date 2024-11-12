# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[Optional[ListNode]]
        :rtype: Optional[ListNode]
        """
        if not lists:
            return None
        if len(lists) == 1:
            return lists[0]
        mid = len(lists) // 2
        left, right = self.mergeKLists(lists[0:mid]), self.mergeKLists(lists[mid:])
        return self.mergeTwo(left, right)
    def mergeTwo(self, first, second):
        dummy = current = ListNode()
        while first and second:
            if first.val < second.val:
                current.next = first
                first = first.next
            else:
                current.next = second
                second = second.next
            current = current.next
        current.next = first or second
        return dummy.next

                    