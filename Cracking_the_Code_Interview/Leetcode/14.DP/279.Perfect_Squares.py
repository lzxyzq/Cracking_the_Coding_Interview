# Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.
''' 
Example 1:

Input: n = 12
Output: 3 
Explanation: 12 = 4 + 4 + 4.
Example 2:

Input: n = 13
Output: 2
Explanation: 13 = 4 + 9. 
'''
class Solution:
    def numSquares(self, n: int):
        DP = [0]
        for i in range(1,n+1):
            DP.append(1+min(DP[i-j*j] for j in range(int(i**.5),0,-1)))
        return DP[n]
