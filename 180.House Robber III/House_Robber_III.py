# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return max(self.Sub_rob(root))

    def Sub_rob(self, root):
        if not root:
            return [0, 0]

        left = self.Sub_rob(root.left)
        right = self.Sub_rob(root.right)

        res = [0, 0]
        res[0] = max(left[0], left[1]) + max(right[0], right[1])
        res[1] = root.val + left[0] + right[0]

        return res
