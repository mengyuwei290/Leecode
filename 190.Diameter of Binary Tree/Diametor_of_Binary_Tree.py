# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0
        self.max_len = 0
        self.max_depth(root)
        return self.max_len
    def max_depth(self, root):
        if not root: return 0
        left = self.max_depth(root.left)
        right = self.max_depth(root.right)
        self.max_len = max(self.max_len, left + right)
        return max(left, right) + 1
