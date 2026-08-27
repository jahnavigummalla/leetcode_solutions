class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price=prices[0]
        maxProfit=float('-inf')
        for price in prices:
            min_price=min(price,min_price)
            maxProfit=max(maxProfit,price-min_price)
        return maxProfit