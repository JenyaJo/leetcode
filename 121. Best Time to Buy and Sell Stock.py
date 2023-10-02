class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        buy = prices[0]

        res = 0
        for i in prices[1:]:
            if i < buy:
                buy = i
            res = max(res, i - buy)
        return res
