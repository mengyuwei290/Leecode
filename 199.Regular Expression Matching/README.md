使用动态规划dp来做， 用一个table来存储匹配的状态， 即：
```
tables = [[False] *(len(s) + 1) for _ in range(len(p) + 1)]
```
由于有*号的存在，需要修复边界：
```
for i in range(2, len(p) + 1):
    tables[i][0] = tables[i-2][0] and p[i-1] == '*'
```
下面就需要迭代遍历所有的可能，一般分成两种情况，
- p[i-1] != "\*", 直接判断s[j-1]和p[i-1]是否匹配即可
- else:
    - 要不是i-1处匹配0个字符，即：tables[i-2][j]；或者匹配多个字符， 即tables[i-1][j]。
    - 当p[i-2] == s[j-1] or p[i-2] == '.'时，tables[i][j] |= tables[i][j-1]
