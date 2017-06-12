观察发现每下边的一层都比上面一层数组长度大1, 而且当前点的值num[i] = pre_num[i-1] + pre_num[i], 其中pre_num是上一层的数组, num是当前的数组, 这里的实现方法就是数组:
```
map(lambda x, y: x+y, pre_num + [0], [0] + pre_num)
```
