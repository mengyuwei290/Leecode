**算法步骤**：
- 判断边界， 当s或words为空时，直接返回[]
- 用散列dt来存储words
- 起始点是i~[0:word_length]，然后j~[i:n:wl]是s序列中词的切片的方式，设置left表示序列的起始点，count表示子序列里word的个数
    - 当s[j:j+wl]在dt中时， 用dt_temp来计数在当前遍历的词频
    - 当dt_temp[str1] > dt[str1]时， 需要将子序列对str1进行截取，
    - 每次判断count == cnt， 即words里的词都遍历完成，res添加left，将left所对应的word在dt_temp进行删除，count--。
