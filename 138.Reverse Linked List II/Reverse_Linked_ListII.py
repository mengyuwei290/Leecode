# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        count = 1
        dummy = jump = ListNode(0)
        dummy.next = head

        while count != m:
            jump = head
            head = head.next
            count += 1

        l, r = head, head
        while count != n + 1:
            r = r.next
            count += 1
        pre, cur = r, l
        for _ in range(n - m + 1):
            cur.next, pre, cur = pre, cur, cur.next
        jump.next = pre

        return dummy.next
