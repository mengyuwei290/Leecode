# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# 法1


class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        stack = [root]
        parent = {root: None}
        while p not in parent or q not in parent:
            node = stack.pop()
            if node.left:
                parent[node.left] = node
                stack.append(node.left)
            if node.right:
                parent[node.right] = node
                stack.append(node.right)
        ancestors = set()
        while p:
            ancestors.add(p)
            p = parent[p]
        while q not in ancestors:
            q = parent[q]
        return q
# 法2


class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        if root in (None, p, q):
            return root
        subs = [self.lowestCommonAncestor(kid, p, q)
                for kid in (root.left, root.right)]
        return root if all(subs) else max(subs)
