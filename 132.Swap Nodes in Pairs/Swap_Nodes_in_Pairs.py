# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head

        while head and head.next:
            temp, head.val = head.val, head.next.val
            head.next.val = temp
            head = head.next.next
        return dummy.next
