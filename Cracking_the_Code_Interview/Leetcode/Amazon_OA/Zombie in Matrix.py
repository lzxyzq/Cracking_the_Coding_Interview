'''
@Author: your name
@Date: 2020-07-11 18:41:53
@LastEditTime: 2020-07-11 21:08:15
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /Cracking_the_Code_Interview/Leetcode/Amazon_OA/Zombie in Matrix.py
'''
# Given a 2D grid, each cell is either a zombie 1 or a human 0. Zombies can turn adjacent (up/down/left/right) human beings into zombies every hour. Find out how many hours does it take to infect all humans?

''' 
Example:
Input:
[[0, 1, 1, 0, 1],
 [0, 1, 0, 1, 0],
 [0, 0, 0, 0, 1],
 [0, 1, 0, 0, 0]]

Output: 2

Explanation:
At the end of the 1st hour, the status of the grid:
[[1, 1, 1, 1, 1],
 [1, 1, 1, 1, 1],
 [0, 1, 0, 1, 1],
 [1, 1, 1, 0, 1]]

At the end of the 2nd hour, the status of the grid:
[[1, 1, 1, 1, 1],
 [1, 1, 1, 1, 1],
 [1, 1, 1, 1, 1],
 [1, 1, 1, 1, 1]] 
'''
rows = 4
columns = 5
grid = [[0, 1, 1, 0, 1],
 [0, 1, 0, 1, 0],
 [0, 0, 0, 0, 1],
 [0, 1, 0, 0, 0]]

def minHour(rows, columns, grid):
    if not rows or not columns:
        return 0
    
    q = [[i,j] for i in range(rows) for j in range(columns) if grid[i][j]==1]
    directions = [[1,0],[-1,0],[0,1],[0,-1]]
    time = 0

    while q:
        new = []
        for [i,j] in q:
            for d in directions:
                ni,nj = i + d[0],j + d[1]
                if 0 <= ni < rows and 0 <= nj < columns and grid[ni][nj] == 0:
                    grid[ni][nj] = 1
                    new.append([ni,nj])
        q = new
        if not q:
            break
        time += 1
    return time
    
if __name__ == '__main__':
    print(minHour(rows, columns, grid))
    



