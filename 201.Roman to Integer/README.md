用散列来存储罗马数字所对应的值， 当
```
d[s[i]] < d[s[i+1]]:
```
res -= d[s[i]], res 的起始值为d[s[len(s)-1]]；
