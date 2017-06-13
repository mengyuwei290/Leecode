2017/06/13: 这道题目还是值得深究的, 目前来说还不是完全的明白
方法用的时双端的DFS,从两端开始逼近, 然后找到连接两端的单词, 进而组成一个字符转换的序列, 我来对每个函数进行解释.

**函数findLadders**:
- 首先, 将wordList转化为集合set(), 并保证endWord在set内, 否则不可能在wordList里转换到endWord, 这种情况下直接返回空的数组->[]
- 创建双端集合fronts = [{beginWord}, {endWord}]
- 创建parent的字典: parent = {beginWord: None, endWord: None}(这是一个ticky, 因为在建立path的时候, 只有beginWord和endWord是没有父节点的, 这可以当做停止条件)
- 假如beginWord和endWord在wordList内的话, 将它删除
- 进入迭代模式, 注意停止条件 while fronts[0] and fronts[1] and not ans, 只要 fronts[0] 或 fronts[1] 为空的话, 判断wordList为空或者当前的转换字符没有在wordList里, 即链条中断; 而 ans有值则说明, 链条已经完成了, 没有必要再继续迭代了;这都时迭代的停止条件.
    - 原则要保证两端的长短均匀, 每次只更新front[0], 当len(front[0]) > len(front[1])话, 交换front[0]和front[1](感觉上这能减少时间复杂度)
    - 更新front[0]

**函数buildLadders**: 当发现front[0]的转换字符在front[1]时, 进入该函数进行双端的连接

**函数_build**: 是函数函数buildLadders调用的子函数, 负责寻找从当前节点到beginWord或者endWord的路劲
