这道题其实很简单，遍历数组所有元素，取m为目前能达到的最大值，取i为当前的位置，当i>m时，判断不能到达，当一直满足i <= m时，最后返回True。