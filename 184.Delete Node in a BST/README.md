先用递归的方法找到需要删除的节点，记为root， root.val的值用root.right.val的值代替，然后将右边的树的root.right.val的值删除， 注意它肯定没有左结点， 所以作为单节点的树进行截枝即可。
