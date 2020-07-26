# Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.



# Method 1 
# Monotonically increasing stack

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


