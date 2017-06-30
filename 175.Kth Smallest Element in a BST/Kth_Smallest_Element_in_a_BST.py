# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        self.count = []
        self.Helper(root)
        return self.count[k - 1]

    def Helper(self, root):
        if not root:
            return

        self.Helper(root.left)
        self.count.append(root.val)
        self.Helper(root.right)
