class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r,maxP = 0,1,0

        while r < len(prices):
            if prices[l] < prices[r]:
                temp = prices[r] - prices[l]
                maxP = max(temp,maxP)
            else:
                l = r
            r+=1
        return maxP
