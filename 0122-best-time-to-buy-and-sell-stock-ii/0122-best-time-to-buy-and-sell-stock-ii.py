class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        sum= 0
        for i in range(1,len(prices)):
            sum+=max(0, prices[i]-prices[i-1])
        
        return sum