这个题目的重点是找到从0_index开始的最长回文，之后将后面剩余的字符串反转加到前面即可。

1. 可以用暴力搜索找反转字符串的在原子字符串的最长子字符串（其实就是找从0开始的最长回文, 比较简单直观, 不做解释）
2. 可用KMP算法求SS = s+'\*'+s.reverse()的table，table的最后一项就是最长回文长度, 这是由于s进行了反转, 反而可以符合KMP算法中匹配的要求了, 即后半s.reverse()中肯定有一个长度的子字符串满足SS[:k] == SS[len(SS) - k:], k 就是table最后一项所示的长度