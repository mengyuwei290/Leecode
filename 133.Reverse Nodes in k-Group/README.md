核心是链表的翻转, 下面是具体的步骤:

- 用dummy记录起始点, 用jump来记录head的前一个node
- 用l, r 来记录当前链表断的左端和右端(不包含右端)
- r计数到右端, 当count == k, 表面需要翻转l, r的链表, 否则, 直接返回dummy.next
- 注意每次翻转后, 需要更新jump, jump.next以及l, jump.next, jump, l = pre, l, r
