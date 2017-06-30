# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        def serialize_helper(node):
            if node:
                vals.append(str(node.val))
                serialize_helper(node.left)
                serialize_helper(node.right)
            else:
                vals.append('#')
        vals = []
        serialize_helper(root)
        return ' '.join(vals)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        def deserialize_helper():
            val = next(vals)
            if val == "#":
                return
            else:
                node = TreeNode(int(val))
                node.left = deserialize_helper()
                node.right = deserialize_helper()
            return node
        vals = iter(data.split())
        return deserialize_helper()


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
