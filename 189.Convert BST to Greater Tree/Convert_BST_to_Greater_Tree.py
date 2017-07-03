# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def inorder(root):
            if not root: return None
            if root.left: inorder(root.left)
            out.append(root)
            if root.right: inorder(root.right)
        out = []
        inorder(root)
        sum = 0
        while out:
            node = out.pop()
            node.val += sum
            sum = node.val
        return root
