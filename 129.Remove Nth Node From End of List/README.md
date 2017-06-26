使用Two Pointers的方法, fast先走n步, 然后slow和fast再同时走, 当fast走到最后一个元素时, slow相应的也走到了从后面数n+1个元素.

**注意**:
- 当开始走n步后的fast为None时, 直接返回head.next即可
