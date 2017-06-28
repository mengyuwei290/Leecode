每个(left, right)对判断left.val是否等于right.val, 假如等于,则继续递归的执行(left.left, right.right) 和 (left.right, right.left); 否则, 则返回False.

注意边界left 或 right为空的处理方式
