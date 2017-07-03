# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root: return []
        def DFS(node):
            if not node: return 0
            sum = node.val
            sum += DFS(node.left) + DFS(node.right)
            d[sum] = d.get(sum,0) + 1
            return sum
        d = {}
        DFS(root)
        max_num = max(d.values())
        return [i for i,v in d.items() if v == max_num]
