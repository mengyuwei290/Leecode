# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        stack = []
        fir_node = sec_node = TreeNode(None)
        pre = TreeNode(float('-inf'))
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            cur = stack.pop()
            if fir_node.val == None and cur.val < pre.val:
                fir_node = pre
            if fir_node.val != None and cur.val < pre.val:
                sec_node = cur
            pre = cur
            root = cur.right
        fir_node.val, sec_node.val = sec_node.val, fir_node.val
