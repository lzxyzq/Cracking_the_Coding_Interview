# Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

# Integers in each row are sorted in ascending from left to right.
# Integers in each column are sorted in ascending from top to bottom.

""" Example:
Consider the following matrix:

[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
Given target = 5, return true.

Given target = 20, return false. 
"""


# Method 1 
# binary search each row




# Method 2 
# traverse along edge

# Starting from the upper right corner, compare the values ​​of target and matrix[i][j]. If it is less than target, the row cannot have this number, so i++; if it is greater than target, then the column cannot have this number, so j--. Encountering a boundary indicates that the matrix contains no targets.

class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        
        i = 0
        j = len(matrix[0]) - 1 
        while(i < len(matrix) and j >= 0):
            num = matrix[i][j]
            if target == num:
                return True
            elif num < target:
                i +=1
            else:
                j -=1
        return False
            
            
