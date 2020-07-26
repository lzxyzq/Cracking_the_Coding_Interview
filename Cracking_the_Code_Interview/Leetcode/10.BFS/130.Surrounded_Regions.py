# Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.

# A region is captured by flipping all 'O's into 'X's in that surrounded region.

""" Example:

X X X X
X O O X
X X O X
X O X X

After running your function, the board should be:

X X X X
X X X X
X X X X
X O X X 
"""
class Solution:
    def solve(self, board: List[List[str]]):
        """
        Do not return anything, modify board in-place instead.
        """
        
        # First append all the corner Os and then do bfs on these values to get the 
	    # neighbor Os. All Os which are connected to any corner O need to be remain 
	    # as O. So replace them with T and then revert it back to O.    
        
        q = []
        if not board:
            return 
        row = len(board)
        col = len(board[0])
    
        for i in range(row):
            for j in range(col):
                if (i == 0 or i == row-1 or j == 0 or j == col -1) and board[i][j] == 'O':
                    q.append((i,j))
        
        while q:
            i,j = q.pop(0)
            board[i][j] = "T"
            for x,y in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
                x_n = i + x
                y_n = j + y
                if x_n >= 0 and x_n < row and y_n >= 0 and y_n < col and board[x_n][y_n] == "O":
                    q.append((x_n, y_n))
                    
        for i in range(row):
            for j in range(col):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "T":
                    board[i][j] = "O"
        
            
                


        
        
        