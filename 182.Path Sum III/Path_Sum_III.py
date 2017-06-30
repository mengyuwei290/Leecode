# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        sum_dict = {0: 1}
        return self.pathSum_helper(root, sum, 0, sum_dict)

    def pathSum_helper(self, root, target, cur_sum, sum_dict):
        if not root:
            return 0

        cur_sum += root.val
        res = sum_dict.get(cur_sum - target, 0)

        sum_dict[cur_sum] = sum_dict.get(cur_sum, 0) + 1

        res += self.pathSum_helper(root.left, target, cur_sum, sum_dict) + \
            self.pathSum_helper(root.right, target, cur_sum, sum_dict)

        sum_dict[cur_sum] = sum_dict.get(cur_sum) - 1

        return res
