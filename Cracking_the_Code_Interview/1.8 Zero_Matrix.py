# Write an algorithm such that if an element in an M*M matrix is 0,its entire row and column are set to 0.
def setZeroes(matrix):
    rownum = len(matrix)
    colnum = len(matrix[0])
    row = [False for i in range(rownum)]
    col = [False for i in range(colnum)]
    for i in range(rownum):
        for j in range(colnum):
            if matrix[i][j] == 0:
                row[i] = True
                col[j] = True
    for i in range(rownum):
        for j in range(colnum):
            if row[i] or col[j]:
                matrix[i][j] = 0



# Utility Function 
def printMatrix(matrix): 
    for row in matrix: 
        print(row) 

# Driver Code 
if __name__ == '__main__': 
    # Test case 1   
    matrix =[  
                [1, 2, 3, 4, 0],
                [6, 0, 8, 9, 10],
                [11, 12, 13, 14, 15],
                [16, 0, 18, 19, 20],
                [21, 22, 23, 24, 25]    
            ] 
    setZeroes(matrix) 
# Print modified matrix 
    printMatrix(matrix) 