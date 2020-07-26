# Say you have an array prices for which the ith element is the price of a given stock on day i.

# Design an algorithm to find the maximum profit. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).

# Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).

# Method 1 Peak Valley Approach
class Solution:
    def maxProfit(self, prices):
        i = 0
        valley = prices[0]
        peak = prices[0]
        max_profit = 0 
        while i < len(prices) - 1:
            while i < len(prices) - 1 and prices[i] >= prices[i+1]:
                i += 1
            valley = prices[i]
            while  i < len(prices) - 1 and prices[i] <= prices[i+1]:
                i += 1
            peak = prices[i]
            max_profit += peak - valley
        return max_profit
        
# Method 2 Simple One Pass
# we can directly keep on adding the difference between the consecutive numbers of the array if the second number is larger than the first one, and at the total sum we obtain will be the maximum profit. 

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0 
        
        total = 0
        for i in range(1,len(prices)):
            if prices[i] > prices[i-1]:
                total += prices[i] - prices[i-1]
        return total

# Time complexity : O(n). Single pass.
# Space complexity : O(1). Constant space required.