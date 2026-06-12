class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        profit = 0
        for right in range(1,len(prices)):
            if prices[left] < prices[right]:
                calculatedProfit = prices[right] - prices[left]
                profit = max(calculatedProfit,profit)
            else:
                left = right
            

        return profit