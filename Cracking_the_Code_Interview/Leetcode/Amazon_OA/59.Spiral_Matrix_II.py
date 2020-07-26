# Given a positive integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.
''' 
Example:

Input: 3
Output:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
] 
'''
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        res = [[0 for _ in range(n)] for _ in range(n)]
        up = 0 
        right = n - 1 
        down = n - 1
        left = 0
        val = 0
        
        while left <= right and up <= down:
            for i in range(left,right+1):
                val += 1 
                res[up][i] = val
            for i in range(up + 1,down + 1):
                val += 1
                res[i][right] = val
            for i in range(right-1,left-1,-1):
                val += 1
                res[down][i] = val
            for i in range(down-1,up,-1):
                val += 1
                res[i][left] = val
            
            up += 1
            down -= 1
            left += 1
            right -= 1
        return res
                
                

    