**算法步骤**:
- root为当前迭代层的最左边点, 它的next指针已设置好(起始的root本来的next指针就是None)
- 为下一层的next设置开始node, dummy, 逐一遍历这一层的node, 将它们的next进行连接
- 更新root到下一层的起始, 即dummy.next
