class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profits, hold = 0, float('-inf')
        for i in prices:
            profits = max(profits, hold + i)
            hold = max(hold, -i)
        return profits
