'''
@Author: your name
@Date: 2020-06-06 21:36:20
@LastEditTime: 2020-06-07 20:46:52
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /Cracking_the_Code_Interview/Leetcode/Array/289.Game_of_Life.py
'''
# According to the Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

# Given a board with m by n cells, each cell has an initial state live (1) or dead (0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

# 1.Any live cell with fewer than two live neighbors dies, as if caused by under-population.
# 2.Any live cell with two or three live neighbors lives on to the next generation.
# 3.Any live cell with more than three live neighbors dies, as if by over-population..
# 4.Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.

# Write a function to compute the next state (after one update) of the board given its current state. The next state is created by applying the above rules simultaneously to every cell in the current state, where births and deaths occur simultaneously.

''' Example:

Input: 
[
  [0,1,0],
  [0,0,1],
  [1,1,1],
  [0,0,0]
]
Output: 
[
  [0,0,0],
  [1,0,1],
  [0,1,1],
  [0,1,0]
] 
'''
# Follow up:

# 1.Could you solve it in-place? Remember that the board needs to be updated at the same time: You cannot update some cells first and then use their updated values to update other cells.
# 2.In this question, we represent the board using a 2D array. In principle, the board is infinite, which would cause problems when the active area encroaches the border of the array. How would you address these problems?

class Solution:
    def gameOfLife(self, board):
        """
        Do not return anything, modify board in-place instead.
        """
        neighbors = [(1,0), (1,-1), (0,-1), (-1,-1), (-1,0), (-1,1), (0,1), (1,1)]
        
        rows = len(board)
        cols = len(board[0])

        copy_board = [[board[row][col] for col in range(cols)] for row in range(rows)]
        
        for row in range(rows):
            for col in range(cols):
                live_neighbors = 0 
                for neighbor in neighbors:
                    r = (row + neighbor[0])
                    c = (col + neighbor[1])
                    if(r < rows and r >= 0) and (c < cols and c >= 0) and (copy_board[r][c] == 1 ):
                        live_neighbors += 1 
                # Rule 1 or Rule 3  
                if copy_board[row][col] == 1 and (live_neighbors < 2 or live_neighbors > 3):
                    board[row][col] = 0
                # Rule 4
                if copy_board[row][col] == 0 and live_neighbors == 3:
                    board[row][col] = 1

# Complexity Analysis

# Time Complexity: O(M×N), where M is the number of rows and N is the number of columns of the Board.

# Space Complexity: O(M×N), where M is the number of rows and N is the number of columns of the Board.This is the space occupied by the copy board we created initially.

# -------------------------------------------------------------------------------------------
class Solution:
    def gameOfLife(self, board):
        
        # Neighbors array to find 8 neighboring cells for a given cell
        neighbors = [(1,0), (1,-1), (0,-1), (-1,-1), (-1,0), (-1,1), (0,1), (1,1)]

        rows = len(board)
        cols = len(board[0])

        # Iterate through board cell by cell.
        for row in range(rows):
            for col in range(cols):

                # For each cell count the number of live neighbors.
                live_neighbors = 0
                for neighbor in neighbors:

                    # row and column of the neighboring cell
                    r = (row + neighbor[0])
                    c = (col + neighbor[1])

                    # Check the validity of the neighboring cell and if it was originally a live cell.
                    if (r < rows and r >= 0) and (c < cols and c >= 0) and abs(board[r][c]) == 1:
                        live_neighbors += 1

                # Rule 1 or Rule 3
                if board[row][col] == 1 and (live_neighbors < 2 or live_neighbors > 3):
                    # -1 signifies the cell is now dead but originally was live.
                    board[row][col] = -1
                # Rule 4
                if board[row][col] == 0 and live_neighbors == 3:
                    # 2 signifies the cell is now live but was originally dead.
                    board[row][col] = 2

        # Get the final representation for the newly updated board.
        for row in range(rows):
            for col in range(cols):
                if board[row][col] > 0:
                    board[row][col] = 1
                else:
                    board[row][col] = 0 

# Complexity Analysis

# Time Complexity: O(M×N), where M is the number of rows and N is the number of columns of the Board.
# Space Complexity: O(1)

# -----------------------------------------------------------------------------------------------------
class Solution:
    def gameOfLifeInfinite(self, live):
        ctr = collections.Counter((I, J) 
                                  for i, j in live 
                                  for I in range(i-1, i+2) 
                                  for J in range(j-1, j+2) 
                                  if I != i or J != j)
        return {ij for ij in ctr if ctr[ij] == 3 or ctr[ij] == 2 and ij in live}

    def gameOfLife(self, board):
        live = {(i, j) for i, row in enumerate(board) for j, live in enumerate(row) if live}
        live = self.gameOfLifeInfinite(live)
        for i, row in enumerate(board):
            for j in range(len(row)):
                row[j] = int((i, j) in live)

