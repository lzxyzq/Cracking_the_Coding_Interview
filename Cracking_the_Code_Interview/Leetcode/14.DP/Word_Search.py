# Given a 2D board and a word, find if the word exists in the grid.

# The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

""" Example:

board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false. 
"""

class Solution:
    def exist(self, board, word) :
        visit = {}
        for i in range(len(board)):
            for j in range(len(board[0])):
                if word[0] == board[i][j]:
                    res = self.dfs(board,visit,i,j,word)
                    if res:
                        return True 
        return False
    def dfs(self,board,visit,i,j,target):
        if len(target) == 0 : #  Stopping Criterion 
            return True
        
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):  # Cross-border, terminal condition
            return False
        
        if visit.get((i, j)):  # Already visited, pruning
            return False
        
        if target[0] != board[i][j]: # Not equal, prune
            return False
        
        visit[(i,j)] = True
        ret = self.dfs(board,visit,i+1,j,target[1:]) or self.dfs(board,visit,i-1,j,target[1:]) or self.dfs(board,visit,i,j+1,target[1:]) or self.dfs(board,visit,i,j-1,target[1:])
        visit[(i,j)] = False
        return ret

                                
if __name__ == '__main__':
    print(Solution().exist([
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
],'K'))
    