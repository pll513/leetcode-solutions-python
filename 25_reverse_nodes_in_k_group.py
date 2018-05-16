# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if k <= 1:
            return head
        n = 0
        phead = ListNode(None)
        phead.next = head
        pcur = phead
        while pcur.next:
            pcur = pcur.next
            n += 1
        groupcnt = n // k
        if groupcnt == 0:
            return head
        curhead = phead
        for i in range(groupcnt):
            pstart = pre = curhead.next
            cur = pre.next
            for j in range(k - 2):
                last = cur
                cur = cur.next
                last.next = pre
                pre = last
            curhead.next = cur
            curhead = pstart
            pstart.next = cur.next
            cur.next = pre
            pstart = pstart.next
        return phead.next
