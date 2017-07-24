使用的dp的方法，每次将当前元素的最长符合条件的序列长度进行记录，之后求序列长度时会根据前面的序列长度进行计算。

**算法核心：**
- 当s[i] == ")"时，更新序列长度
- 根据s[i-1] == "(" 或 s[i-1] == ")"分成两种情况来讨论最长子序列的长度