# Given n, how many structurally unique BST's (binary search trees) that store values 1 ... n?

''' Example:

Input: 3
Output: 5
Explanation:
Given n = 3, there are a total of 5 unique BST's:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
'''
class Solution:
    def numTrees(self, n: int) -> int:
        dp = {0:1, 1:1, 2:2}
        if n < 3: 
            return dp[n]
        for i in range(3, n+1):
            num = 0
            for j in range(i):
                num += dp[j]*dp[i-j-1]
            dp[i] = num
        return dp[n]