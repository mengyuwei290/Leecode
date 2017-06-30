我们要的是p和q分别在root的不同方向, 而代码:
```
(root.val - p.val) * (root.val - q.val) > 0
```
表示p,q都在root的一边,需要下潜, root = (root.left, root.right)[p.val > root.val]代表下潜的方向.
