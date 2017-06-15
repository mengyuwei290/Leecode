# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack, res, pre = [], [], None
        while root or stack:
            if root:
                stack.append(root)
                root = root.left
            elif stack[-1].right != pre:
                root = stack[-1].right
                pre = None
            else:
                pre = stack.pop()
                res.append(pre.val)
        return res
