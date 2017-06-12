# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if inorder:
            i = inorder.index(preorder[0])
            node = TreeNode(preorder[0])
            node.left = self.buildTree(preorder[1:i + 1], inorder[:i])
            node.right = self.buildTree(preorder[i + 1:], inorder[i + 1:])
            return node
