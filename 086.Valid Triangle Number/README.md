三角形的判别规则: 任意两边的和大于第三边, 我们采用two Pointers的思想, 先将数组进行排序, 然后固定最高位, 在最高位前面进行two pointers的遍历.

**注意**:
- 当满足三角形的判决规制的时候, 说明一共有r-l个满足条件的三角形
- 注意要一直保持 l < r
