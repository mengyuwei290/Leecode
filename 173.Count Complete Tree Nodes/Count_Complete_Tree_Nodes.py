# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        left_Depth = self.getDepth(root.left)
        right_Depth = self.getDepth(root.right)

        if left_Depth == right_Depth:
            return pow(2, left_Depth) + self.countNodes(root.right)
        else:
            return pow(2, right_Depth) + self.countNodes(root.left)

    def getDepth(self, root):
        if not root:
            return 0
        return 1 + self.getDepth(root.left)
