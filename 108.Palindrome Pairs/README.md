算法的思想是: 切割一个字符, 当一半(任意一个)的翻转在word_dict可以找到, 另一半本身就是回文, 那么我们就找到了一对.

**步骤**:
- 创建word_dict, key为每个word, value为每个字符的坐标
- 对每个字符找它相应的对
    - 将word[i] 切分成 tmp1 = word[i][:j] 和 tmp2 = word[i][j:], 注意j的范围是[0:len(word[i]) + 1]
    - 寻找 tmp1 + tmp2 + tmp1[::-1]的组合
    - 寻找 tmp2[::-1] + tmp1 + tmp2, 在这里注意j != 0 的边界条件, 因为这会造成重复的(i, j)
