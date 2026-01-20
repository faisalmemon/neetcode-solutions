class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        lowest_seen = float('inf')

        for price in prices:
            if price < lowest_seen:
                lowest_seen = price
            max_profit = max(max_profit, price - lowest_seen)
        return max_profit 
