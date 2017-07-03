# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root: return []
        def dfs(node):
            if not node: return
            count[node.val] = count.get(node.val, 0) + 1
            dfs(node.left)
            dfs(node.right)

        count = {}
        dfs(root)
        max_count = max(count.values())
        return [i for i,v in count.items() if v == max_count]
