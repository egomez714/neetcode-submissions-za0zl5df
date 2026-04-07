class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        price = 0
        l = 0
        biggest = 0
        for r in range(len(prices)):
            if prices[r] < prices[l]:
                while prices[l] > prices[r]:
                    l+= 1
            price = prices[r] - prices[l]
            biggest = max(price,biggest)
        return biggest
