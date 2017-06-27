# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if not head:
            return None

        slow, fast = head, head.next
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        fast = slow.next
        slow.next = None
        pre = None
        while fast:
            fast.next, pre, fast = pre, fast, fast.next
        slow, fast = head, pre
        while slow:
            if fast:
                slow.next, fast.next, slow, fast = fast, slow.next, slow.next, fast.next
            else:
                slow = slow.next
