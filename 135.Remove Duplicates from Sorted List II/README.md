根据r.val != head.val找到右边界, 判断count > 1的话, 说明有重复的元素, 那么更新jump.next, 否则, 更新jump(jump表示已遍历过且去除重复后链表的最后一个元素).
