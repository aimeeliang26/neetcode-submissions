class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # you are given an integer array prices
        # prices[i] is the price of neetcoin on ith day 

        # if none future price is greater than current price, 
        # return 0 

        # we want to find the max difference 
        # O(n) time 
        l, r = 0, 1
        maxProfit = 0 

        while r < len(prices):
            if prices[l] < prices[r]:
                maxProfit = max(prices[r]-prices[l], maxProfit)
                
                r += 1
            else:
                l = r 
                r += 1
        return maxProfit