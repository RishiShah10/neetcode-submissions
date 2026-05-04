class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy,sell = 0,1
        maxProfit = 0
        while sell < len(prices):
            print(buy,sell, "buy and sell")
            pProfit = prices[sell] - prices[buy]
            if pProfit >= 0:
                maxProfit = max(maxProfit, pProfit)
            else:
                buy = sell
            sell += 1
        return maxProfit
        