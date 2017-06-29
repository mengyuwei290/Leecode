# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        stack = []
        cur = root
        pre = TreeNode(0)
        pre.right = cur
        while cur or stack:
            while cur:
                if cur.right:
                    stack.append(cur.right)
                left, cur.left = cur.left, None
                pre, pre.right, cur = cur, left, left
            if stack:
                cur = stack.pop()
            pre.right = cur
