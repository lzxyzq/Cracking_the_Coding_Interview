# Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.


# Method 1 
# Monotonically increasing stack

# 单调栈的运用，使用一个单调递增栈来维护已经出现了的矩形高度。

# 如果后面新来的元素高度比栈顶元素高，那么需要入栈，因为面积最大的元素会出现在后面。
# 如果后面新来的元素高度比栈顶元素小，那么需要弹出栈里的元素，并且，每次弹出的时候都要对计算目前的宽度，相乘得到面积。
# 栈里保存索引的方式是需要掌握的，保存索引的方式在最小值栈结构中也有运用。

# 每次求栈内矩形的宽度的时候，其实是求其位置到最右边的距离。注意即将入栈的元素索引 i 是一直不变的，另外栈里的每个元素的索引可以认为是矩形的左边界。


class Solution:
    def largestRectangleArea(self, heights):
        stack = []
        res = 0 
        heights.append(0)
        n = len(heights) 
        
        for i in range(n):
            if not stack or heights[i] > heights[stack[-1]]:
                stack.append(i) 
            else:
                while stack and heights[i] <= heights[stack[-1]]:
                    h = heights[stack[-1]] 
                    stack.pop()
                    w = i if not stack else i - stack[-1] - 1
                    res = max(res, h * w)
                stack.append(i)
        return res

if __name__ == '__main__':
    heights = [2, 1, 5, 6, 2, 3]

    solution = Solution()
    res = solution.largestRectangleArea(heights)
    print(res)
