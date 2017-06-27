# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        la, lb = self.Length_of_List(headA), self.Length_of_List(headB)
        if la < lb:
            headA, headB = headB, headA
            la, lb = lb, la
        count = 0
        while count != (la - lb):
            count += 1
            headA = headA.next
        while headA and headB:
            if headA == headB:
                return headA
            headA, headB = headA.next, headB.next
        return None

    def Length_of_List(self, head):
        count = 0
        while head:
            count += 1
            head = head.next
        return count
