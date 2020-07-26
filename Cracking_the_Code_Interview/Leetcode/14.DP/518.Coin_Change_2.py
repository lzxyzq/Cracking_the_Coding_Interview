# You are given coins of different denominations and a total amount of money. Write a function to compute the number of combinations that make up that amount. You may assume that you have infinite number of each kind of coin.
""" 
Example 1:

Input: amount = 5, coins = [1, 2, 5]
Output: 4
Explanation: there are four ways to make up the amount:
5=5
5=2+2+1
5=2+1+1+1
5=1+1+1+1+1
Example 2:

Input: amount = 3, coins = [2]
Output: 0
Explanation: the amount of 3 cannot be made up just with coins of 2.
Example 3:

Input: amount = 10, coins = [10] 
Output: 1 
"""
# Backtracking  (Time Limit Exceeded)
class Solution:
    def change(self, amount, coins):
        result = []
        coins.sort()
        self.helper(coins,[],result,amount)
        return result
    def helper(self,coins,path,result,target):
        if target == 0:
            result.append(path)
        for i in range(len(coins)):
            residue = target - coins[i]
            if residue < 0:
                break
            self.helper(coins[i:],path+[coins[i]],result,residue)
if __name__ == '__main__':
    print(Solution().change(100,[3,5,7,8,9,10]))
    
# DP
# dp[i]表示组成钱数i的不同方法。
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1
        for i in coins:
            for j in range(amount+1):
                if j >= i:
                    dp[j] += dp[j-i]
        return dp[-1]