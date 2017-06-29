# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None


class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if not root:
            return
        dummy = TreeLinkNode(0)
        while root:
            dummy.next = None
            temp = dummy
            while root:
                if root.left:
                    temp.next = root.left
                    temp = temp.next
                if root.right:
                    temp.next = root.right
                    temp = temp.next
                root = root.next
            root = dummy.next
