class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        curr = 0
        left, right = 0, 1

        while right < len(prices):
            curr = prices[right] - prices[left]
            if curr < 0:
                left = right
            else:
                profit = max(profit, curr)
            right += 1
        return profit