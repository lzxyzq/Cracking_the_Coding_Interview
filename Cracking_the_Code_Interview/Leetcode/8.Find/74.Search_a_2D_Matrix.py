'''
@Author: your name
@Date: 2020-06-22 01:05:10
@LastEditTime: 2020-06-22 15:16:25
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /Cracking_the_Code_Interview/Leetcode/Find/74.Search_a_2D_Matrix.py
'''
# Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

# Integers in each row are sorted from left to right.
# The first integer of each row is greater than the last integer of the previous row.
""" Example 1:

Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 3
Output: true
Example 2:

Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 13
Output: false
"""
# Method 1: brute force
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == target:
                    return i, j

# Time: O(mn)
# Space: O(1)


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        # (1) start with the first row and run binary search in each row
        i = 0
        row = len(matrix) 
        col = len(matrix[0])
        while i < row and target >= matrix[i][0]:
            low = 0
            high = col - 1
            while low <= high:
                mid = low + (high-low)//2
                if target > matrix[i][mid]:
                    low = mid + 1
                elif target < matrix[i][mid]:
                    high = mid - 1 
                else:
                    return target == matrix[i][mid]
            i += 1 
        return False

# Time: O(mlogn)
# Space: O(1)