# Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return the reordered list.

# The first node is considered odd, and the second node is even, and so on.

# Note that the relative order inside both the even and odd groups should remain as it was in the input.

# You must solve the problem in O(1) extra space complexity and O(n) time complexity.

 

# Example 1:


# Input: head = [1,2,3,4,5]
# Output: [1,3,5,2,4]
# Definition for singly-linked list.

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        current, last = head, None
        oddEnd = head
        while current != None:
            # insert odd to head
            ovenHead = oddEnd.next 
            currentNext = current.next
            current.next = ovenHead
            if current != head:
                oddEnd.next = current
                oddEnd = current

            # repair oven link
            if last:
                last.next = currentNext

            # go to next odd node
            if not currentNext:
                break
            current = currentNext.next
            last = currentNext
        return head

tmp = ListNode(5, None)
tmp = ListNode(4, tmp)
tmp = ListNode(3, tmp)
tmp = ListNode(2, tmp)
tmp = ListNode(1, tmp)

sol = Solution()
res = sol.oddEvenList(tmp)