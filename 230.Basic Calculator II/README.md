使用stack来存储每个数字的符号, 在处理 "+" 或者 "-"号的时候只需要将当前的num的符号进行改变即可, 而在处理 "\*" 或 "/" 的时候, 需要将stack之前的数弹出, 进行计算后再压入stack.

注意, 字符串符号必须没有空符" ", 还有边界条件.
