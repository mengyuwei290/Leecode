时间复杂度O(N), 空间复杂度O(N). 用散列来记录每个词的次数, 用count来记录次的总个数.

**注意**:
- 有词长度的起始方式, 即i = range(0, wl)
- count <= cnt, 当不满足时, 注意更新