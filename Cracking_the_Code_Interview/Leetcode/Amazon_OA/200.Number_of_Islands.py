# Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

''' 
Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3 
'''
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        if m == 0:
            return 0 
        n = len(grid[0])
        
        ans = 0 
        for x in range(m):
            for y in range(n):
                if grid[x][y] == '1':
                    ans += 1
                    self.dfs(grid,x,y,n,m)
        return ans
    
    def dfs(self,grid,x,y,n,m):
        if (x<0 or y <0 or x>=m or y>=n or grid[x][y] == '0'):
            return 
        grid[x][y] = '0'
        self.dfs(grid,x+1,y,n,m)
        self.dfs(grid,x-1,y,n,m)
        self.dfs(grid,x,y-1,n,m)
        self.dfs(grid,x,y+1,n,m)