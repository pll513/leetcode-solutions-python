# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        p1 = p2 = head
        while n > 0:
            if p1.next:
                p1 = p1.next
                n -= 1
            else:
                break
        if n > 0:
            head = head.next
            return head
        while p1.next:
            p1 = p1.next
            p2 = p2.next
        p2.next = p2.next.next
        return head
