先将list中每个链表的表头提取出来, 用(node.val, node)来构造优先序列(最小堆), 然后每次从序列中弹出一个值来更新node, 假如该node还有next, 再构造(node.next.val,  node.next)压入序列中, 直到序列长度为0.
