递归执行(DFS的核心算法):
```
1 + max(map(self.maxDepth, (root.left, root.right))) if root else 0
```
