# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack, res = [], []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            pre = stack.pop()
            res.append(pre.val)
            root = pre.right
        return res
