'''
@Author: your name
@Date: 2020-06-02 22:10:09
@LastEditTime: 2020-06-02 22:55:10
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /Cracking_the_Code_Interview/Leetcode/Array/48.Rotate_Image.py
'''
# You are given an n x n 2D matrix representing an image.Rotate the image by 90 degrees (clockwise).

''' 
Example 1:

Given input matrix = 
[
  [1,2,3],
  [4,5,6],
  [7,8,9]
],

rotate the input matrix in-place such that it becomes:
[
  [7,4,1],
  [8,5,2],
  [9,6,3]
]
Example 2:

Given input matrix =
[
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
], 

rotate the input matrix in-place such that it becomes:
[
  [15, 13, 2, 5],
  [14, 3, 4, 1],
  [12, 6, 8, 9],
  [16, 7,10, 11]
]
'''

class Solution:
    def rotate(self, matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """
        if matrix:
            row = len(matrix)
            col = len(matrix[0])
            
            for i in range(row//2):
                for j in range(col):
                    matrix[row-i-1][j],matrix[i][j] = matrix[i][j],matrix[row-i-1][j]
            for i in range(row):
                for j in range(i):
                    matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]