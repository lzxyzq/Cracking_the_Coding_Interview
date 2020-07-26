# Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

''' 
Example:

Input: 

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0

Output: 4 
'''

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        row, col = len(matrix), len(matrix[0])
        max_edge_length = 0
        for i in range(col):
            matrix[0][i] = int(matrix[0][i])
        for i in range(row):
            matrix[i][0] = int(matrix[i][0])
        for i in range(row):
            for j in range(col):
                if i > 0 and j > 0:
                    if matrix[i][j] == '1':
                        matrix[i][j] = 1 + min( matrix[i][j-1], matrix[i-1][j-1], matrix[i-1][j])
                    else:
                        matrix[i][j] = 0
                max_edge_length = max(max_edge_length, matrix[i][j])
        return max_edge_length**2
                    
            