class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        maxele = prices[len(prices)-1]
        for i in prices[::-1]:
            if(i<maxele):
                profit = max(profit,maxele-i)
            else:
                maxele = i
        
        return profit
        
