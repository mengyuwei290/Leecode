由于卖在买之后, 所以将profits放在hold之前, 通过:
```
profits = max(profits, hold + i)
hold = max(hold, -i)
```
实现算法.
