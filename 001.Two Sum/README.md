这个题目用Hash Table来做， Hash Table的时间复杂度为O(N), 空间复杂的也为O(N)。

利用了哈希表查找key的时间复杂的为O(1)，以target-num的值创建key，将当前的下标号存入key所对应的value，当遍历到某个元素的值cur等于某个key时，这就说明(dict[key], cur.index)就是我们要求的一组答案。
