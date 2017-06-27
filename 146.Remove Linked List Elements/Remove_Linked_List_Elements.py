# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        dummy = pre = ListNode(0)
        dummy.next = head
        while head:
            if head.val == val:
                if head.next:
                    head.val, head.next = head.next.val, head.next.next
                else:
                    pre.next = head = None
            else:
                pre = head
                head = head.next
        return dummy.next
