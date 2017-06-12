其实是045的一个衍生, 第i次的交易基础时前i-1的收益, 所以有hold[i] = max(hold[i], release[i-1] - stock[i]), 注意越后的hold越在函数的前面, 保证时间的有序性.
