# Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = []
        for row_num in range(numRows):
            row = [None for _ in range(row_num+1)]
            row[0], row[-1] = 1, 1
            for j in range(1, len(row)-1):
                row[j] = result[row_num-1][j-1] + result[row_num-1][j]
            result.append(row)
        return result 

# Time complexity : O(numRows^2)
# Space complexity : O(numRows^2)


# 第0行一个数字
# 第1行两个数字
# ……
# 每行的数字都是1开头,每行的长度为行数加1.
# 初始化需要行的大小[1] + [0]*rowIndex
# 迭代每一行，从每行最后一个数字开始计算。 result[j] = result[j] + result[j-1]


