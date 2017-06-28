# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return root == None or self.isSymmetric_helper(root.left, root.right)

    def isSymmetric_helper(self, left, right):
        if not left or not right:
            return left == right
        if left.val != right.val:
            return False
        return self.isSymmetric_helper(left.left, right.right) and self.isSymmetric_helper(left.right, right.left)
