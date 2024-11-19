class Solution(object):
    def maxProfit(self, prices):
        buy = prices[0]
        profit = 0
        for i in range(1, len(prices)): 
            if prices[i] < buy: 
                buy = prices[i]
            elif prices[i] - buy > profit: 
                profit = prices[i] - buy 
        return profit 

