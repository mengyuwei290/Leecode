# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = odd = ListNode(0)
        dummy2 = even = ListNode(0)
        while head and head.next:
            odd.next = head
            even.next = head.next
            odd, even, head = odd.next, even.next, head.next.next
            odd.next, even.next = None, None
        if head:
            odd.next = head
            odd = head
        odd.next = dummy2.next
        return dummy.next
