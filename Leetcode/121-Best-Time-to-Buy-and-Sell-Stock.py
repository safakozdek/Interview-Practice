class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        size = len(prices)
        if size < 2:
            return 0
        profit = 0
        current = 99999999
        for price in prices:
            current = min(current, price)
            if current < price:
                profit = max(price - current, profit)

        return profit
