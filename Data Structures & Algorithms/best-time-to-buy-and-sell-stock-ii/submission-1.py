class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        prev = prices[0]
        buy = prev
        for p in prices:
            if prev > p:
                profit = prev - buy
                res += profit
                buy = p
            prev = p
        res += (prev - buy)
        return res if res else prev - buy