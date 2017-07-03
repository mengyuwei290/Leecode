# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root: return []
        level = [root]
        res = []
        while level:
            res.append(max(map(lambda x: x.val, level)))
            level = [kid for node in level for kid in (node.left,node.right) if kid]
        return res
