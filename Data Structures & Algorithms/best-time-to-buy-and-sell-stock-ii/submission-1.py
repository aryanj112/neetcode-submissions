class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        res = 0
        
        for i, n in enumerate(prices):
            if i == 0:
                continue
            if n > prices[i-1]:
                res += n - prices[i-1]

        return res