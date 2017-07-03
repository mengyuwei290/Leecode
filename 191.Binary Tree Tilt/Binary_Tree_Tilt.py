# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.all_tilt = 0
        self.DFS_tilt(root)
        return self.all_tilt
    def DFS_tilt(self, root):
        if not root: return 0
        left = self.DFS_tilt(root.left)
        right = self.DFS_tilt(root.right)

        tilt = abs(left-right)
        self.all_tilt += tilt
        return root.val + left + right
