递归的DFS先达到叶节点, 然后返回当前路径的sum, 中间节点总合每个节点的left_sum和right_sum, 注意当不是叶节点时, 返回0.