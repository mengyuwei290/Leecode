算一道偏难的题目了,其中构建转换的字符使用了hash表, 从begin到end的探索使用了DFS,时间复杂度O(N!)(基本不可能吧,最坏情况).

**注意**:
- 使用visited集合来记忆哪些字符已经路过
- 用双端队列来存储字符, 因为我们要从低位pop已经经过的元素, 从高位append没有经过的元素, 这样的操作用deque来做比较好
- 每次在queue加入字符时,一定要保证当前的字符没在visited里
