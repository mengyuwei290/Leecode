# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.max_value = float('-inf')
        self.PathDown(root)
        return self.max_value

    def PathDown(self, root):
        if not root:
            return 0
        left = max(0, self.PathDown(root.left))
        right = max(0, self.PathDown(root.right))
        self.max_value = max(self.max_value, left + right + root.val)
        return max(left, right) + root.val
