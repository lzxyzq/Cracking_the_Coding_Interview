
# The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.

# Given an integer n, return all distinct solutions to the n-queens puzzle.

# Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space respectively.

""" Example:
Input: 4
Output: [
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]
"""
# ideas:
# Use the DFS helper function to find solutions recursively. A solution will be found when the length of queen_y is equal to n (queen_y is a list of the indices of the queens).

# In this problem, whenever a location (x, y) is occupied, any other locations (p, q ) where p + q == x + y or p - q == x - y would be invalid. We can use this information to keep track of the indicators (sum_x_y and xyminus_x_y_sum ) of the invalid positions and then call DFS recursively with valid positions only.

# 不能同行同列对角线,因为是逐行找可行的Y位置,X不存在重复.限制条件仅为不同列不同对角线。

class Solution:
    def solveNQueens(self, n: int) :
        res = []
        self.helper([],[],[],n,res)
        return [["."*i + "Q" + "."*(n-i-1) for i in sol] for sol in res]
    
    def helper(self,queen_y,sum_x_y,minus_x_y,n,res):
        x=len(queen_y)
        if x == n:
            res.append(queen_y)
            return
        for y in range(n):
            if y not in queen_y and x+y not in sum_x_y and x-y not in minus_x_y:
                self.helper([y]+queen_y,[x+y]+sum_x_y,[x-y]+minus_x_y,n,res)
               
  