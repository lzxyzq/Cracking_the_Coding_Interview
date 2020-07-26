# Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.
""" Example 1:

Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:

Input:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
Output: [1,2,3,4,8,12,11,10,9,5,6,7] 
"""

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return []
        row = len(matrix)
        col = len(matrix[0])
        res = matrix[0]
        
        if row > 1 :
            for i in range(1,row):
                res.append(matrix[i][col-1])
            for j in range(col-2,-1,-1):
                res.append(matrix[row-1][j])
            if col > 1:
                for i in range(row-2,0,-1):
                    res.append(matrix[i][0])
        M = []
        for k in range(1,row-1):
            t = matrix[k][1:-1]
            M.append(t)
        return res + self.spiralOrder(M)
            
