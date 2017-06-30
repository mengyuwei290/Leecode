# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        view = []
        if root:
            level = [root]
            while level:
                view += [level[-1].val]
                level = [kid for node in level for kid in (
                    node.left, node.right) if kid]
        return view
