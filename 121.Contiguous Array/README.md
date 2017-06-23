这道题的trick是, 当不同的坐标count[i]和count[j]一样时, 说明在[i+1, j+1]的数有相同的0和1的数目, 直接j-i就得到了这个连续子序列的长度, 更新max_length即可.
