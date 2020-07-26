# A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
# The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).
# Now consider if some obstacles are added to the grids. How many unique paths would there be?

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]):
        row = len(obstacleGrid)
        col = len(obstacleGrid[0])
        for i in range(row):
            for j in range(col):
                if obstacleGrid[i][j] == 1:
                    obstacleGrid[i][j] = 0
                else:
                    if i - 1 >= 0 and j - 1 >= 0:
                        obstacleGrid[i][j] = obstacleGrid[i-1][j] + obstacleGrid[i][j-1]
                    elif i - 1 >= 0:
                        obstacleGrid[i][j] = obstacleGrid[i-1][j]
                    elif j - 1 >= 0:
                        obstacleGrid[i][j] = obstacleGrid[i][j-1]
                    else:
                        obstacleGrid[i][j] = 1 # obstacleGrid[1][1]
        return obstacleGrid[-1][-1]
                        
          
        