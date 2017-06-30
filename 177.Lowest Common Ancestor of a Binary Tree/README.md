法1:
- 使用字典存储每个节点的parents, 直到p和q都在字典中
- 然后用set来存储p的所有parent
- 在set找q的parent, 不在的话令q=parents[q]

法2:
- 利用当left, right都不为None时, 返回root, 否则, 返回不为None的那个节点.
