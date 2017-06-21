# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None


class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        dummy = RandomListNode(0)
        dummy.next = head
        while head:
            Next = head.next
            head.next = RandomListNode(head.label)
            head.next.next = Next
            head.next.random = None
            head = Next

        head = dummy.next
        while head:
            if head.random:
                head.next.random = head.random.next
            head = head.next.next

        head = dummy.next
        copyed_head = None
        while head:
            if not copyed_head:
                copyed_head = head.next
                pt = copyed_head
            else:
                pt.next = head.next
                pt = pt.next
            head.next = head.next.next
            head = head.next
        return copyed_head
