# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        res, stack, temp, flag = [], [root], [], 1
        while(stack):
            level_size = len(stack)
            for i in range(level_size):
                node = stack.pop(0)
                temp += [node.val]
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)
            res += [temp[::flag]]
            temp = []
            flag *= -1
        return res
