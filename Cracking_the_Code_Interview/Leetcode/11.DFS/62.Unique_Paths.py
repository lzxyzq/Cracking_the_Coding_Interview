# A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

# The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

# How many possible unique paths are there?

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        table = [[0 for x in range(n)] for x in range(m)]
        for i in range(m):
            table[i][0] = 1
        for i in range(n):
            table[0][i] = 1
        for i in range(1,m):
            for j in range(1,n):
                table[i][j] = table[i-1][j] + table[i][j-1]
        return table[m-1][n-1]