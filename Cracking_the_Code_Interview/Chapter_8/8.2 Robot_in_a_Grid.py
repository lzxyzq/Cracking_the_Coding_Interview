# Imaging a robot sitting on the upper left corner of grid with r rows and c columns.The robot can only move in two directions, right and down,but certain cells are "off limits" such that the robot cannot step on them.Design an algorithm to find a path for the robot from top left to the bottom right. 
# 62. Unique Paths (leetcode)
# 63. Unique Paths II (leetcode)

def uniquePathsWithObstacles(obstacleGrid):
    """
    :type obstacleGrid: List[List[int]]
    :rtype: int
    """
    m, n = len(obstacleGrid), len(obstacleGrid[0])
    
    for i in range(m):
        for j in range(n):
            if obstacleGrid[i][j] == 1:
                obstacleGrid[i][j] = 0 
            else:
                if i-1 >= 0 and j-1 >= 0:
                    obstacleGrid[i][j] = obstacleGrid[i-1][j]+obstacleGrid[i][j-1]
                elif i-1 >= 0:
                    obstacleGrid[i][j] = obstacleGrid[i-1][j]
                elif j-1 >= 0:
                    obstacleGrid[i][j] = obstacleGrid[i][j-1]
                else:
                    obstacleGrid[i][j] = 1
    
    return obstacleGrid[m-1][n-1]


allPaths = [] 
def findPaths(maze,m,n): 
    path = [0 for d in range(m+n-1)] 
    findPathsUtil(maze,m,n,0,0,path,0) 
      
def findPathsUtil(maze,m,n,i,j,path,indx): 
    global allPaths 
    # if we reach the bottom of maze, we can only move right 
    if i==m-1: 
        for k in range(j,n): 
            #path.append(maze[i][k]) 
            path[indx+k-j] = [i,k] 
        # if we hit this block, it means one path is completed.  
        # Add it to paths list and print 
        print(path) 
        allPaths.append(path) 
        return
    # if we reach to the right most corner, we can only move down 
    if j == n-1: 
        for k in range(i,m): 
            path[indx+k-i] = [k,j] 
        #  path.append(maze[j][k]) 
        # if we hit this block, it means one path is completed.  
        # Add it to paths list and print 
        print(path) 
        allPaths.append(path) 
        return
      
    # add current element to the path list 
    #path.append(maze[i][j]) 
    path[indx] = [i,j] 
      
    # move down in y direction and call findPathsUtil recursively 
    findPathsUtil(maze, m, n, i+1, j, path, indx+1) 
      
    # move down in y direction and call findPathsUtil recursively 
    findPathsUtil(maze, m, n, i, j+1, path, indx+1) 
  
if __name__ == '__main__': 
    maze = [[1,2,3], 
            [4,5,6], 
            [7,8,9]] 
    findPaths(maze,3,3) 
    print(allPaths) 