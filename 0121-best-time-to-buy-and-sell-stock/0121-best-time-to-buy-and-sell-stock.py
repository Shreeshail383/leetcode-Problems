class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        mini = prices[0]
        maxProfit = 0
        n = len(prices)
        for i in range(n):
            cost = prices[i] - mini
            maxProfit = max(maxProfit, cost)
            mini = min(mini, prices[i])
        return maxProfit