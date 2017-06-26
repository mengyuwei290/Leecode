# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = jump = ListNode(0)
        dummy.next = r = head

        while head:
            count = 0
            while r and r.val == head.val:
                count += 1
                r = r.next
            if count > 1:
                jump.next = r
            else:
                jump = head
            head = r
        return dummy.next
