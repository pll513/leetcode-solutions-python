# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        ptr1 = l1
        ptr2 = l2
        ptr3 = None
        l3 = None
        carry = 0
        while ptr1 and ptr2:
            sum = ptr1.val + ptr2.val + carry
            carry = sum // 10
            if ptr3:
                ptr3.next = ListNode(sum % 10)
                ptr3 = ptr3.next
            else:
                ptr3 = l3 = ListNode(sum % 10)
            ptr1 = ptr1.next
            ptr2 = ptr2.next

        ptr = ptr1 if ptr1 else ptr2
        while ptr:
            sum = ptr.val + carry
            carry = sum // 10
            if ptr3:
                ptr3.next = ListNode(sum % 10)
                ptr3 = ptr3.next
            else:
                ptr3 = l3 = ListNode(sum % 10)
            ptr = ptr.next
            
        if carry:
            ptr3.next = ListNode(1)
            
        return l3