# Given an image represented by an N*N matrix, where each pixel in the image is 4 bytes, write a method rotate the image by 90 degrees.Can you do this in place?
def rotate(matrix):
    if matrix:
        rows = len(matrix)
        cols = len(matrix[0])
        for i in range(rows // 2):
            for j in range(cols):
                matrix[i][j], matrix[rows - i - 1][j] = matrix[rows - i - 1][j], matrix[i][j]
        for i in range(rows):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

# Utility Function 
def printMatrix(mat): 
    for row in mat: 
        print (row) 

# Driver Code 
if __name__ == '__main__': 
# Test case 1 
    matrix =[  
                [1,  2,  3,  4 ], 
                [5,  6,  7,  8 ], 
                [9,  10, 11, 12 ], 
                [13, 14, 15, 16 ]   
            ] 
    rotate(matrix)
    # Print modified matrix 
    printMatrix(matrix) 
